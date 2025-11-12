#!/usr/bin/env python3
# flake8: noqa
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer",
#     "rich",
#     "platformdirs",
#     "readchar",
#     "httpx",
# ]
# ///
"""
NUAA CLI - AI-Assisted Project Management for NGOs

Usage:
    uvx --from git+https://github.com/zophiezlan/spec-driven-projects.git nuaa init <project-name>
    uvx --from git+https://github.com/zophiezlan/spec-driven-projects.git nuaa init .
    uvx --from git+https://github.com/zophiezlan/spec-driven-projects.git nuaa init --here

Or install globally (via package name):
    uv tool install --from . nuaa-cli
    nuaa init <project-name>
    nuaa init .
    nuaa init --here

Legacy alias: the "specify" command still works for backwards compatibility.
"""

import os
import subprocess
import sys
import zipfile
import tempfile
import shutil
import shlex
import json
from pathlib import Path
from typing import Optional, Tuple
import re
from datetime import datetime, timezone

import typer
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.live import Live
from rich.align import Align
from rich.table import Table
from rich.tree import Tree
from typer.core import TyperGroup

# For cross-platform keyboard input
import readchar
import ssl
import truststore

ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)


def _github_token(cli_token: str | None = None) -> str | None:
    """Return sanitized GitHub token (cli arg takes precedence) or None."""
    return ((cli_token or os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or "").strip()) or None


def _github_auth_headers(cli_token: str | None = None) -> dict:
    """Return Authorization header dict only when a non-empty token exists."""
    token = _github_token(cli_token)
    return {"Authorization": f"Bearer {token}"} if token else {}


def _parse_rate_limit_headers(headers: httpx.Headers) -> dict:
    """Extract and parse GitHub rate-limit headers."""
    info = {}

    # Standard GitHub rate-limit headers
    if "X-RateLimit-Limit" in headers:
        info["limit"] = headers.get("X-RateLimit-Limit")
    if "X-RateLimit-Remaining" in headers:
        info["remaining"] = headers.get("X-RateLimit-Remaining")
    if "X-RateLimit-Reset" in headers:
        reset_epoch = int(headers.get("X-RateLimit-Reset", "0"))
        if reset_epoch:
            reset_time = datetime.fromtimestamp(reset_epoch, tz=timezone.utc)
            info["reset_epoch"] = reset_epoch
            info["reset_time"] = reset_time
            info["reset_local"] = reset_time.astimezone()

    # Retry-After header (seconds or HTTP-date)
    if "Retry-After" in headers:
        retry_after = headers.get("Retry-After")
        try:
            info["retry_after_seconds"] = int(retry_after)
        except ValueError:
            # HTTP-date format - not implemented, just store as string
            info["retry_after"] = retry_after

    return info


def _format_rate_limit_error(status_code: int, headers: httpx.Headers, url: str) -> str:
    """Format a user-friendly error message with rate-limit information."""
    rate_info = _parse_rate_limit_headers(headers)

    lines = [f"GitHub API returned status {status_code} for {url}"]
    lines.append("")

    if rate_info:
        lines.append("[bold]Rate Limit Information:[/bold]")
        if "limit" in rate_info:
            lines.append(f"  • Rate Limit: {rate_info['limit']} requests/hour")
        if "remaining" in rate_info:
            lines.append(f"  • Remaining: {rate_info['remaining']}")
        if "reset_local" in rate_info:
            reset_str = rate_info["reset_local"].strftime("%Y-%m-%d %H:%M:%S %Z")
            lines.append(f"  • Resets at: {reset_str}")
        if "retry_after_seconds" in rate_info:
            lines.append(f"  • Retry after: {rate_info['retry_after_seconds']} seconds")
        lines.append("")

    # Add troubleshooting guidance
    lines.append("[bold]Troubleshooting Tips:[/bold]")
    lines.append("  • If you're on a shared CI or corporate environment, you may be rate-limited.")
    lines.append(
        "  • Consider using a GitHub token via --github-token or the GH_TOKEN/GITHUB_TOKEN"
    )
    lines.append("    environment variable to increase rate limits.")
    lines.append(
        "  • Authenticated requests have a limit of 5,000/hour vs 60/hour for unauthenticated."
    )

    return "\n".join(lines)


# ------------------------------
# Utility helpers for NUAA files
# ------------------------------


def _slugify(text: str) -> str:
    """Convert text to a filesystem-friendly slug."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return re.sub(r"^-+|-+$", "", text) or "feature"


def _find_templates_root(start: Path | None = None) -> Path:
    """Find .nuaa/templates or nuaa-kit/templates directory by walking up from start (or CWD)."""
    search_origin = start or Path.cwd()

    candidates: list[Path] = []
    for path in [search_origin, *search_origin.parents]:
        candidates.append(path / ".nuaa" / "templates")
        candidates.append(path / "nuaa-kit" / "templates")

    repo_root = Path(__file__).parent.parent.parent
    candidates.append(repo_root / ".nuaa" / "templates")
    candidates.append(repo_root / "nuaa-kit" / "templates")

    for candidate in candidates:
        if candidate.is_dir():
            return candidate

    raise FileNotFoundError(
        "Could not locate '.nuaa/templates' or 'nuaa-kit/templates'. Run 'nuaa init' first or ensure NUAA templates are available."
    )


def _ensure_nuaa_root(root: Path | None = None) -> Path:
    """Ensure the 'nuaa' directory exists under the project root (current dir by default)."""
    if root is None:
        root = Path.cwd()
    nuaa_root = root / "nuaa"
    nuaa_root.mkdir(parents=True, exist_ok=True)
    return nuaa_root


def _next_feature_dir(program_name: str, root: Path | None = None) -> tuple[Path, str, str]:
    """Compute next feature directory 'nuaa/NNN-slug' and return (path, num_str, slug)."""
    nuaa_root = _ensure_nuaa_root(root)
    # Find highest NNN prefix
    highest = 0
    for child in nuaa_root.iterdir() if nuaa_root.exists() else []:
        if child.is_dir():
            m = re.match(r"^(\d{3})-", child.name)
            if m:
                try:
                    highest = max(highest, int(m.group(1)))
                except ValueError:
                    pass
    next_num = highest + 1
    num_str = f"{next_num:03d}"
    slug = _slugify(program_name)
    feature_dir = nuaa_root / f"{num_str}-{slug}"
    feature_dir.mkdir(parents=True, exist_ok=True)
    return feature_dir, num_str, slug


def _find_feature_dir_by_program(program_name: str, root: Path | None = None) -> Path | None:
    """Try to find an existing feature dir whose slug starts with the program name slug."""
    nuaa_root = _ensure_nuaa_root(root)
    slug = _slugify(program_name)
    for child in sorted(nuaa_root.iterdir()) if nuaa_root.exists() else []:
        if child.is_dir() and re.search(rf"-\b{re.escape(slug)}\b", child.name):
            return child
    return None


def _load_template(name: str) -> str:
    """Load a template file from the discovered NUAA templates directory."""
    templates_root = _find_templates_root()
    path = templates_root / name
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {name}")
    return path.read_text(encoding="utf-8")


def _apply_replacements(text: str, mapping: dict[str, str]) -> str:
    """Apply simple placeholder replacements supporting both [Placeholders] and {{TOKENS}}."""
    out = text
    # Bracket placeholders used in templates
    bracket_map = {
        "[Name]": mapping.get("PROGRAM_NAME", ""),
        "[Description]": mapping.get("TARGET_POPULATION", ""),
        "[Timeframe]": mapping.get("DURATION", ""),
        "[Date]": mapping.get("DATE", datetime.now().strftime("%Y-%m-%d")),
    }
    for k, v in bracket_map.items():
        out = out.replace(k, v)
    # Curly token replacements
    for k, v in mapping.items():
        out = out.replace(f"{{{{{k}}}}}", v)
    return out


def _prepend_metadata(text: str, metadata: dict[str, str]) -> str:
    """Prepend a YAML-style metadata block to markdown text."""
    lines = ["---"]
    for k, v in metadata.items():
        lines.append(f"{k}: {v}")
    lines.append("---\n")
    return "\n".join(lines) + text


def _write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _stamp() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


# Agent configuration with name, folder, install URL, and CLI tool requirement
AGENT_CONFIG = {
    "copilot": {
        "name": "GitHub Copilot",
        "folder": ".github/agents/",
        "install_url": None,  # IDE-based, no CLI check needed
        "requires_cli": False,
    },
    "claude": {
        "name": "Claude Code",
        "folder": ".claude/",
        "install_url": "https://docs.anthropic.com/en/docs/claude-code/setup",
        "requires_cli": True,
    },
    "gemini": {
        "name": "Gemini CLI",
        "folder": ".gemini/",
        "install_url": "https://github.com/google-gemini/gemini-cli",
        "requires_cli": True,
    },
    "cursor-agent": {
        "name": "Cursor",
        "folder": ".cursor/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "qwen": {
        "name": "Qwen Code",
        "folder": ".qwen/",
        "install_url": "https://github.com/QwenLM/qwen-code",
        "requires_cli": True,
    },
    "opencode": {
        "name": "opencode",
        "folder": ".opencode/",
        "install_url": "https://opencode.ai",
        "requires_cli": True,
    },
    "codex": {
        "name": "Codex CLI",
        "folder": ".codex/",
        "install_url": "https://github.com/openai/codex",
        "requires_cli": True,
    },
    "windsurf": {
        "name": "Windsurf",
        "folder": ".windsurf/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "kilocode": {
        "name": "Kilo Code",
        "folder": ".kilocode/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "auggie": {
        "name": "Auggie CLI",
        "folder": ".augment/",
        "install_url": "https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli",
        "requires_cli": True,
    },
    "codebuddy": {
        "name": "CodeBuddy",
        "folder": ".codebuddy/",
        "install_url": "https://www.codebuddy.ai/cli",
        "requires_cli": True,
    },
    "roo": {
        "name": "Roo Code",
        "folder": ".roo/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "q": {
        "name": "Amazon Q Developer CLI",
        "folder": ".amazonq/",
        "install_url": "https://aws.amazon.com/developer/learning/q-developer-cli/",
        "requires_cli": True,
    },
    "amp": {
        "name": "Amp",
        "folder": ".agents/",
        "install_url": "https://ampcode.com/manual#install",
        "requires_cli": True,
    },
}

SCRIPT_TYPE_CHOICES = {"sh": "POSIX Shell (bash/zsh)", "ps": "PowerShell"}

CLAUDE_LOCAL_PATH = Path.home() / ".claude" / "local" / "claude"

BANNER = """
███╗   ██╗██╗   ██╗ █████╗  █████╗ 
████╗  ██║██║   ██║██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║███████║███████║
██║╚██╗██║██║   ██║██╔══██║██╔══██║
██║ ╚████║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
"""

TAGLINE = "NUAA Project - AI-Assisted Project Management for NSW Users and AIDS Association"


class StepTracker:
    """Track and render hierarchical steps without emojis, similar to Claude Code tree output.
    Supports live auto-refresh via an attached refresh callback.
    """

    def __init__(self, title: str):
        self.title = title
        self.steps = []  # list of dicts: {key, label, status, detail}
        self.status_order = {
            "pending": 0,
            "running": 1,
            "done": 2,
            "error": 3,
            "skipped": 4,
        }
        self._refresh_cb = None  # callable to trigger UI refresh

    def attach_refresh(self, cb):
        self._refresh_cb = cb

    def add(self, key: str, label: str):
        if key not in [s["key"] for s in self.steps]:
            self.steps.append({"key": key, "label": label, "status": "pending", "detail": ""})
            self._maybe_refresh()

    def start(self, key: str, detail: str = ""):
        self._update(key, status="running", detail=detail)

    def complete(self, key: str, detail: str = ""):
        self._update(key, status="done", detail=detail)

    def error(self, key: str, detail: str = ""):
        self._update(key, status="error", detail=detail)

    def skip(self, key: str, detail: str = ""):
        self._update(key, status="skipped", detail=detail)

    def _update(self, key: str, status: str, detail: str):
        for s in self.steps:
            if s["key"] == key:
                s["status"] = status
                if detail:
                    s["detail"] = detail
                self._maybe_refresh()
                return

        self.steps.append({"key": key, "label": key, "status": status, "detail": detail})
        self._maybe_refresh()

    def _maybe_refresh(self):
        if self._refresh_cb:
            try:
                self._refresh_cb()
            except Exception:
                pass

    def render(self):
        tree = Tree(f"[cyan]{self.title}[/cyan]", guide_style="grey50")
        for step in self.steps:
            label = step["label"]
            detail_text = step["detail"].strip() if step["detail"] else ""

            status = step["status"]
            if status == "done":
                symbol = "[green]●[/green]"
            elif status == "pending":
                symbol = "[green dim]○[/green dim]"
            elif status == "running":
                symbol = "[cyan]○[/cyan]"
            elif status == "error":
                symbol = "[red]●[/red]"
            elif status == "skipped":
                symbol = "[yellow]○[/yellow]"
            else:
                symbol = " "

            if status == "pending":
                # Entire line light gray (pending)
                if detail_text:
                    line = f"{symbol} [bright_black]{label} ({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [bright_black]{label}[/bright_black]"
            else:
                # Label white, detail (if any) light gray in parentheses
                if detail_text:
                    line = f"{symbol} [white]{label}[/white] [bright_black]({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [white]{label}[/white]"

            tree.add(line)
        return tree


def get_key():
    """Get a single keypress in a cross-platform way using readchar."""
    key = readchar.readkey()

    if key == readchar.key.UP or key == readchar.key.CTRL_P:
        return "up"
    if key == readchar.key.DOWN or key == readchar.key.CTRL_N:
        return "down"

    if key == readchar.key.ENTER:
        return "enter"

    if key == readchar.key.ESC:
        return "escape"

    if key == readchar.key.CTRL_C:
        raise KeyboardInterrupt

    return key


def select_with_arrows(
    options: dict, prompt_text: str = "Select an option", default_key: str | None = None
) -> str:
    """
    Interactive selection using arrow keys with Rich Live display.

    Args:
        options: Dict with keys as option keys and values as descriptions
        prompt_text: Text to show above the options
        default_key: Default option key to start with

    Returns:
        Selected option key
    """
    option_keys = list(options.keys())
    if default_key and default_key in option_keys:
        selected_index = option_keys.index(default_key)
    else:
        selected_index = 0

    selected_key = None

    def create_selection_panel():
        """Create the selection panel with current selection highlighted."""
        table = Table.grid(padding=(0, 2))
        table.add_column(style="cyan", justify="left", width=3)
        table.add_column(style="white", justify="left")

        for i, key in enumerate(option_keys):
            if i == selected_index:
                table.add_row("▶", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")
            else:
                table.add_row(" ", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")

        table.add_row("", "")
        table.add_row("", "[dim]Use ↑/↓ to navigate, Enter to select, Esc to cancel[/dim]")

        return Panel(
            table,
            title=f"[bold]{prompt_text}[/bold]",
            border_style="cyan",
            padding=(1, 2),
        )

    console.print()

    def run_selection_loop():
        nonlocal selected_key, selected_index
        with Live(
            create_selection_panel(),
            console=console,
            transient=True,
            auto_refresh=False,
        ) as live:
            while True:
                try:
                    key = get_key()
                    if key == "up":
                        selected_index = (selected_index - 1) % len(option_keys)
                    elif key == "down":
                        selected_index = (selected_index + 1) % len(option_keys)
                    elif key == "enter":
                        selected_key = option_keys[selected_index]
                        break
                    elif key == "escape":
                        console.print("\n[yellow]Selection cancelled[/yellow]")
                        raise typer.Exit(1)

                    live.update(create_selection_panel(), refresh=True)

                except KeyboardInterrupt:
                    console.print("\n[yellow]Selection cancelled[/yellow]")
                    raise typer.Exit(1)

    run_selection_loop()

    if selected_key is None:
        console.print("\n[red]Selection failed.[/red]")
        raise typer.Exit(1)

    return selected_key


console = Console()


class BannerGroup(TyperGroup):
    """Custom group that shows banner before help."""

    def format_help(self, ctx, formatter):
        # Show banner before help
        show_banner()
        super().format_help(ctx, formatter)


app = typer.Typer(
    name="nuaa",
    help="NUAA Project Kit - AI-assisted NGO program management (built on Spec-Driven Development)",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)


def show_banner():
    """Display the ASCII art banner."""
    banner_lines = BANNER.strip().split("\n")
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]

    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)

    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()


@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    if ctx.invoked_subcommand is None and "--help" not in sys.argv and "-h" not in sys.argv:
        show_banner()
        console.print(Align.center("[dim]Run 'nuaa --help' for usage information[/dim]"))
        console.print()


def run_command(
    cmd: list[str],
    check_return: bool = True,
    capture: bool = False,
    shell: bool = False,
) -> Optional[str]:
    """Run a shell command and optionally capture output."""
    try:
        if capture:
            result = subprocess.run(
                cmd, check=check_return, capture_output=True, text=True, shell=shell
            )
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=check_return, shell=shell)
            return None
    except subprocess.CalledProcessError as e:
        if check_return:
            console.print(f"[red]Error running command:[/red] {' '.join(cmd)}")
            console.print(f"[red]Exit code:[/red] {e.returncode}")
            if hasattr(e, "stderr") and e.stderr:
                console.print(f"[red]Error output:[/red] {e.stderr}")
            raise
        return None


def check_tool(tool: str, tracker: StepTracker | None = None) -> bool:
    """Check if a tool is installed. Optionally update tracker.

    Args:
        tool: Name of the tool to check
        tracker: Optional StepTracker to update with results

    Returns:
        True if tool is found, False otherwise
    """
    # Special handling for Claude CLI after `claude migrate-installer`
    # See: https://github.com/github/spec-kit/issues/123
    # The migrate-installer command REMOVES the original executable from PATH
    # and creates an alias at ~/.claude/local/claude instead
    # This path should be prioritized over other claude executables in PATH
    if tool == "claude":
        if CLAUDE_LOCAL_PATH.exists() and CLAUDE_LOCAL_PATH.is_file():
            if tracker:
                tracker.complete(tool, "available")
            return True

    found = shutil.which(tool) is not None

    if tracker:
        if found:
            tracker.complete(tool, "available")
        else:
            tracker.error(tool, "not found")

    return found


def is_git_repo(path: Path | None = None) -> bool:
    """Check if the specified path is inside a git repository."""
    if path is None:
        path = Path.cwd()

    if not path.is_dir():
        return False

    try:
        # Use git command to check if inside a work tree
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_git_repo(project_path: Path, quiet: bool = False) -> Tuple[bool, Optional[str]]:
    """Initialize a git repository in the specified path.

    Args:
        project_path: Path to initialize git repository in
        quiet: if True suppress console output (tracker handles status)

    Returns:
        Tuple of (success: bool, error_message: Optional[str])
    """
    original_cwd = Path.cwd()
    try:
        os.chdir(project_path)
        if not quiet:
            console.print("[cyan]Initializing git repository...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit from NUAA template"],
            check=True,
            capture_output=True,
            text=True,
        )
        if not quiet:
            console.print("[green]✓[/green] Git repository initialized")
        return True, None

    except subprocess.CalledProcessError as e:
        error_msg = f"Command: {' '.join(e.cmd)}\nExit code: {e.returncode}"
        if e.stderr:
            error_msg += f"\nError: {e.stderr.strip()}"
        elif e.stdout:
            error_msg += f"\nOutput: {e.stdout.strip()}"

        if not quiet:
            console.print(f"[red]Error initializing git repository:[/red] {e}")
        return False, error_msg
    finally:
        os.chdir(original_cwd)


def handle_vscode_settings(sub_item, dest_file, rel_path, verbose=False, tracker=None) -> None:
    """Handle merging or copying of .vscode/settings.json files."""

    def log(message, color="green"):
        if verbose and not tracker:
            console.print(f"[{color}]{message}[/] {rel_path}")

    try:
        with open(sub_item, "r", encoding="utf-8") as f:
            new_settings = json.load(f)

        if dest_file.exists():
            merged = merge_json_files(dest_file, new_settings, verbose=verbose and not tracker)
            with open(dest_file, "w", encoding="utf-8") as f:
                json.dump(merged, f, indent=4)
                f.write("\n")
            log("Merged:", "green")
        else:
            shutil.copy2(sub_item, dest_file)
            log("Copied (no existing settings.json):", "blue")

    except Exception as e:
        log(f"Warning: Could not merge, copying instead: {e}", "yellow")
        shutil.copy2(sub_item, dest_file)


def merge_json_files(existing_path: Path, new_content: dict, verbose: bool = False) -> dict:
    """Merge new JSON content into existing JSON file.

    Performs a deep merge where:
    - New keys are added
    - Existing keys are preserved unless overwritten by new content
    - Nested dictionaries are merged recursively
    - Lists and other values are replaced (not merged)

    Args:
        existing_path: Path to existing JSON file
        new_content: New JSON content to merge in
        verbose: Whether to print merge details

    Returns:
        Merged JSON content as dict
    """
    try:
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, just use new content
        return new_content

    def deep_merge(base: dict, update: dict) -> dict:
        """Recursively merge update dict into base dict."""
        result = base.copy()
        for key, value in update.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                result[key] = deep_merge(result[key], value)
            else:
                # Add new key or replace existing value
                result[key] = value
        return result

    merged = deep_merge(existing_content, new_content)

    if verbose:
        console.print(f"[cyan]Merged JSON file:[/cyan] {existing_path.name}")

    return merged


def download_template_from_github(
    ai_assistant: str,
    download_dir: Path,
    *,
    script_type: str = "sh",
    verbose: bool = True,
    show_progress: bool = True,
    client: httpx.Client | None = None,
    debug: bool = False,
    github_token: str | None = None,
) -> Tuple[Path, dict]:
    # NUAA templates are published as release assets in this repository
    repo_owner = "zophiezlan"
    repo_name = "spec-driven-projects"
    close_client = False
    http_client = client
    if http_client is None:
        http_client = httpx.Client(verify=ssl_context)
        close_client = True

    if verbose:
        console.print("[cyan]Fetching latest release information...[/cyan]")
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    try:
        response = http_client.get(
            api_url,
            timeout=30,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        )
        status = response.status_code
        if status != 200:
            # Format detailed error message with rate-limit info
            error_msg = _format_rate_limit_error(status, response.headers, api_url)
            if debug:
                error_msg += f"\n\n[dim]Response body (truncated 500):[/dim]\n{response.text[:500]}"
            raise RuntimeError(error_msg)
        try:
            release_data = response.json()
        except ValueError as je:
            raise RuntimeError(
                f"Failed to parse release JSON: {je}\nRaw (truncated 400): {response.text[:400]}"
            )
    except Exception as e:
        console.print(f"[red]Error fetching release information[/red]")
        console.print(Panel(str(e), title="Fetch Error", border_style="red"))
        raise typer.Exit(1)

    assets = release_data.get("assets", [])
    # Expected asset name pattern: nuaa-template-<agent>-<script>-<version>.zip
    pattern = f"nuaa-template-{ai_assistant}-{script_type}"
    matching_assets = [
        asset for asset in assets if pattern in asset["name"] and asset["name"].endswith(".zip")
    ]

    asset = matching_assets[0] if matching_assets else None

    if asset is None:
        console.print(
            f"[red]No matching release asset found[/red] for [bold]{ai_assistant}[/bold] (expected pattern: [bold]{pattern}[/bold])"
        )
        asset_names = [a.get("name", "?") for a in assets]
        console.print(
            Panel(
                "\n".join(asset_names) or "(no assets)",
                title="Available Assets",
                border_style="yellow",
            )
        )
        raise typer.Exit(1)

    download_url = asset["browser_download_url"]
    filename = asset["name"]
    file_size = asset["size"]

    if verbose:
        console.print(f"[cyan]Found template:[/cyan] {filename}")
        console.print(f"[cyan]Size:[/cyan] {file_size:,} bytes")
        console.print(f"[cyan]Release:[/cyan] {release_data['tag_name']}")

    zip_path = download_dir / filename
    if verbose:
        console.print(f"[cyan]Downloading template...[/cyan]")

    try:
        with http_client.stream(
            "GET",
            download_url,
            timeout=60,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        ) as response:
            if response.status_code != 200:
                # Handle rate-limiting on download as well
                error_msg = _format_rate_limit_error(
                    response.status_code, response.headers, download_url
                )
                if debug:
                    error_msg += (
                        f"\n\n[dim]Response body (truncated 400):[/dim]\n{response.text[:400]}"
                    )
                raise RuntimeError(error_msg)
            total_size = int(response.headers.get("content-length", 0))
            with open(zip_path, "wb") as f:
                if total_size == 0:
                    for chunk in response.iter_bytes(chunk_size=8192):
                        f.write(chunk)
                else:
                    if show_progress:
                        with Progress(
                            SpinnerColumn(),
                            TextColumn("[progress.description]{task.description}"),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                            console=console,
                        ) as progress:
                            task = progress.add_task("Downloading...", total=total_size)
                            downloaded = 0
                            for chunk in response.iter_bytes(chunk_size=8192):
                                f.write(chunk)
                                downloaded += len(chunk)
                                progress.update(task, completed=downloaded)
                    else:
                        for chunk in response.iter_bytes(chunk_size=8192):
                            f.write(chunk)
        if verbose:
            console.print(f"Downloaded: {filename}")
        metadata = {
            "filename": filename,
            "size": file_size,
            "release": release_data["tag_name"],
            "asset_url": download_url,
        }
        return zip_path, metadata
    except Exception as e:
        console.print(f"[red]Error downloading template[/red]")
        detail = str(e)
        if zip_path.exists():
            zip_path.unlink()
        console.print(Panel(detail, title="Download Error", border_style="red"))
        raise typer.Exit(1)
    finally:
        if close_client:
            http_client.close()


def download_and_extract_template(
    project_path: Path,
    ai_assistant: str,
    script_type: str,
    is_current_dir: bool = False,
    *,
    verbose: bool = True,
    tracker: StepTracker | None = None,
    client: httpx.Client | None = None,
    debug: bool = False,
    github_token: str | None = None,
) -> Path:
    """Download the latest release and extract it to create a new project.
    Returns project_path. Uses tracker if provided (with keys: fetch, download, extract, cleanup)
    """
    current_dir = Path.cwd()

    if tracker:
        tracker.start("fetch", "contacting GitHub API")
    try:
        zip_path, meta = download_template_from_github(
            ai_assistant,
            current_dir,
            script_type=script_type,
            verbose=verbose and tracker is None,
            show_progress=(tracker is None),
            client=client,
            debug=debug,
            github_token=github_token,
        )
        if tracker:
            tracker.complete("fetch", f"release {meta['release']} ({meta['size']:,} bytes)")
            tracker.add("download", "Download template")
            tracker.complete("download", meta["filename"])
    except Exception as e:
        if tracker:
            tracker.error("fetch", str(e))
        else:
            if verbose:
                console.print(f"[red]Error downloading template:[/red] {e}")
        raise

    if tracker:
        tracker.add("extract", "Extract template")
        tracker.start("extract")
    elif verbose:
        console.print("Extracting template...")

    try:
        if not is_current_dir:
            project_path.mkdir(parents=True)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_contents = zip_ref.namelist()
            if tracker:
                tracker.start("zip-list")
                tracker.complete("zip-list", f"{len(zip_contents)} entries")
            elif verbose:
                console.print(f"[cyan]ZIP contains {len(zip_contents)} items[/cyan]")

            if is_current_dir:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    zip_ref.extractall(temp_path)

                    extracted_items = list(temp_path.iterdir())
                    if tracker:
                        tracker.start("extracted-summary")
                        tracker.complete("extracted-summary", f"temp {len(extracted_items)} items")
                    elif verbose:
                        console.print(
                            f"[cyan]Extracted {len(extracted_items)} items to temp location[/cyan]"
                        )

                    source_dir = temp_path
                    if len(extracted_items) == 1 and extracted_items[0].is_dir():
                        source_dir = extracted_items[0]
                        if tracker:
                            tracker.add("flatten", "Flatten nested directory")
                            tracker.complete("flatten")
                        elif verbose:
                            console.print(f"[cyan]Found nested directory structure[/cyan]")

                    for item in source_dir.iterdir():
                        dest_path = project_path / item.name
                        if item.is_dir():
                            if dest_path.exists():
                                if verbose and not tracker:
                                    console.print(
                                        f"[yellow]Merging directory:[/yellow] {item.name}"
                                    )
                                for sub_item in item.rglob("*"):
                                    if sub_item.is_file():
                                        rel_path = sub_item.relative_to(item)
                                        dest_file = dest_path / rel_path
                                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                                        # Special handling for .vscode/settings.json - merge instead of overwrite
                                        if (
                                            dest_file.name == "settings.json"
                                            and dest_file.parent.name == ".vscode"
                                        ):
                                            handle_vscode_settings(
                                                sub_item,
                                                dest_file,
                                                rel_path,
                                                verbose,
                                                tracker,
                                            )
                                        else:
                                            shutil.copy2(sub_item, dest_file)
                            else:
                                shutil.copytree(item, dest_path)
                        else:
                            if dest_path.exists() and verbose and not tracker:
                                console.print(f"[yellow]Overwriting file:[/yellow] {item.name}")
                            shutil.copy2(item, dest_path)
                    if verbose and not tracker:
                        console.print(f"[cyan]Template files merged into current directory[/cyan]")
            else:
                zip_ref.extractall(project_path)

                extracted_items = list(project_path.iterdir())
                if tracker:
                    tracker.start("extracted-summary")
                    tracker.complete("extracted-summary", f"{len(extracted_items)} top-level items")
                elif verbose:
                    console.print(
                        f"[cyan]Extracted {len(extracted_items)} items to {project_path}:[/cyan]"
                    )
                    for item in extracted_items:
                        console.print(f"  - {item.name} ({'dir' if item.is_dir() else 'file'})")

                if len(extracted_items) == 1 and extracted_items[0].is_dir():
                    nested_dir = extracted_items[0]
                    temp_move_dir = project_path.parent / f"{project_path.name}_temp"

                    shutil.move(str(nested_dir), str(temp_move_dir))

                    project_path.rmdir()

                    shutil.move(str(temp_move_dir), str(project_path))
                    if tracker:
                        tracker.add("flatten", "Flatten nested directory")
                        tracker.complete("flatten")
                    elif verbose:
                        console.print(f"[cyan]Flattened nested directory structure[/cyan]")

    except Exception as e:
        if tracker:
            tracker.error("extract", str(e))
        else:
            if verbose:
                console.print(f"[red]Error extracting template:[/red] {e}")
                if debug:
                    console.print(Panel(str(e), title="Extraction Error", border_style="red"))

        if not is_current_dir and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)
    else:
        if tracker:
            tracker.complete("extract")
    finally:
        if tracker:
            tracker.add("cleanup", "Remove temporary archive")

        if zip_path.exists():
            zip_path.unlink()
            if tracker:
                tracker.complete("cleanup")
            elif verbose:
                console.print(f"Cleaned up: {zip_path.name}")

    return project_path


def ensure_executable_scripts(project_path: Path, tracker: StepTracker | None = None) -> None:
    """Ensure POSIX .sh scripts under agent script folders have execute bits (no-op on Windows)."""
    if os.name == "nt":
        return  # Windows: skip silently
    # Default to a common scripts folder if present; skip quietly if not
    scripts_root = project_path / ".agents" / "scripts"
    if not scripts_root.is_dir():
        return
    failures: list[str] = []
    updated = 0
    for script in scripts_root.rglob("*.sh"):
        try:
            if script.is_symlink() or not script.is_file():
                continue
            try:
                with script.open("rb") as f:
                    if f.read(2) != b"#!":
                        continue
            except Exception:
                continue
            st = script.stat()
            mode = st.st_mode
            if mode & 0o111:
                continue
            new_mode = mode
            if mode & 0o400:
                new_mode |= 0o100
            if mode & 0o040:
                new_mode |= 0o010
            if mode & 0o004:
                new_mode |= 0o001
            if not (new_mode & 0o100):
                new_mode |= 0o100
            os.chmod(script, new_mode)
            updated += 1
        except Exception as e:
            failures.append(f"{script.relative_to(scripts_root)}: {e}")
    if tracker:
        detail = f"{updated} updated" + (f", {len(failures)} failed" if failures else "")
        tracker.add("chmod", "Set script permissions recursively")
        (tracker.error if failures else tracker.complete)("chmod", detail)
    else:
        if updated:
            console.print(
                f"[cyan]Updated execute permissions on {updated} script(s) recursively[/cyan]"
            )
        if failures:
            console.print("[yellow]Some scripts could not be updated:[/yellow]")
            for f in failures:
                console.print(f"  - {f}")


@app.command()
def init(
    project_name: str | None = typer.Argument(
        None,
        help="Name for your new project directory (optional if using --here, or use '.' for current directory)",
    ),
    ai_assistant: str | None = typer.Option(
        None,
        "--ai",
        help="AI assistant to use: claude, gemini, copilot, cursor-agent, qwen, opencode, codex, windsurf, kilocode, auggie, codebuddy, amp, or q",
    ),
    script_type: str | None = typer.Option(None, "--script", help="Script type to use: sh or ps"),
    ignore_agent_tools: bool = typer.Option(
        False,
        "--ignore-agent-tools",
        help="Skip checks for AI agent tools like Claude Code",
    ),
    no_git: bool = typer.Option(False, "--no-git", help="Skip git repository initialization"),
    here: bool = typer.Option(
        False,
        "--here",
        help="Initialize project in the current directory instead of creating a new one",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force merge/overwrite when using --here (skip confirmation)",
    ),
    skip_tls: bool = typer.Option(
        False, "--skip-tls", help="Skip SSL/TLS verification (not recommended)"
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Show verbose diagnostic output for network and extraction failures",
    ),
    github_token: str | None = typer.Option(
        None,
        "--github-token",
        help="GitHub token to use for API requests (or set GH_TOKEN or GITHUB_TOKEN environment variable)",
    ),
):
    """
    Initialize a new NUAA Project Kit workspace from the latest template.

    This command will:
    1. Check that required tools are installed (git is optional)
    2. Let you choose your AI assistant
    3. Download the appropriate template from GitHub
    4. Extract the template to a new project directory or current directory
    5. Initialize a fresh git repository (if not --no-git and no existing repo)
    6. Optionally set up AI assistant commands

    Examples:
        specify init my-project
        specify init my-project --ai claude
        specify init my-project --ai copilot --no-git
        specify init --ignore-agent-tools my-project
        specify init . --ai claude         # Initialize in current directory
        specify init .                     # Initialize in current directory (interactive AI selection)
        specify init --here --ai claude    # Alternative syntax for current directory
        specify init --here --ai codex
        specify init --here --ai codebuddy
        specify init --here
        specify init --here --force  # Skip confirmation when current directory not empty
    """

    show_banner()

    if project_name == ".":
        here = True
        project_name = None  # Clear project_name to use existing validation logic

    if here and project_name:
        console.print("[red]Error:[/red] Cannot specify both project name and --here flag")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print(
            "[red]Error:[/red] Must specify either a project name, use '.' for current directory, or use --here flag"
        )
        raise typer.Exit(1)

    if here:
        project_name = Path.cwd().name
        project_path = Path.cwd()

        existing_items = list(project_path.iterdir())
        if existing_items:
            console.print(
                f"[yellow]Warning:[/yellow] Current directory is not empty ({len(existing_items)} items)"
            )
            console.print(
                "[yellow]Template files will be merged with existing content and may overwrite existing files[/yellow]"
            )
            if force:
                console.print(
                    "[cyan]--force supplied: skipping confirmation and proceeding with merge[/cyan]"
                )
            else:
                response = typer.confirm("Do you want to continue?")
                if not response:
                    console.print("[yellow]Operation cancelled[/yellow]")
                    raise typer.Exit(0)
    else:
        assert project_name is not None  # for type checkers
        project_path = Path(project_name).resolve()
        if project_path.exists():
            error_panel = Panel(
                f"Directory '[cyan]{project_name}[/cyan]' already exists\n"
                "Please choose a different project name or remove the existing directory.",
                title="[red]Directory Conflict[/red]",
                border_style="red",
                padding=(1, 2),
            )
            console.print()
            console.print(error_panel)
            raise typer.Exit(1)

    current_dir = Path.cwd()

    setup_lines = [
        "[cyan]Specify Project Setup[/cyan]",
        "",
        f"{'Project':<15} [green]{project_path.name}[/green]",
        f"{'Working Path':<15} [dim]{current_dir}[/dim]",
    ]

    if not here:
        setup_lines.append(f"{'Target Path':<15} [dim]{project_path}[/dim]")

    console.print(Panel("\n".join(setup_lines), border_style="cyan", padding=(1, 2)))

    should_init_git = False
    if not no_git:
        should_init_git = check_tool("git")
        if not should_init_git:
            console.print("[yellow]Git not found - will skip repository initialization[/yellow]")

    if ai_assistant:
        if ai_assistant not in AGENT_CONFIG:
            console.print(
                f"[red]Error:[/red] Invalid AI assistant '{ai_assistant}'. Choose from: {', '.join(AGENT_CONFIG.keys())}"
            )
            raise typer.Exit(1)
        selected_ai = ai_assistant
    else:
        # Create options dict for selection (agent_key: display_name)
        ai_choices = {key: config["name"] for key, config in AGENT_CONFIG.items()}
        selected_ai = select_with_arrows(ai_choices, "Choose your AI assistant:", "copilot")

    if not ignore_agent_tools:
        agent_config = AGENT_CONFIG.get(selected_ai)
        if agent_config and agent_config["requires_cli"]:
            install_url = agent_config["install_url"]
            if not check_tool(selected_ai):
                error_panel = Panel(
                    f"[cyan]{selected_ai}[/cyan] not found\n"
                    f"Install from: [cyan]{install_url}[/cyan]\n"
                    f"{agent_config['name']} is required to continue with this project type.\n\n"
                    "Tip: Use [cyan]--ignore-agent-tools[/cyan] to skip this check",
                    title="[red]Agent Detection Error[/red]",
                    border_style="red",
                    padding=(1, 2),
                )
                console.print()
                console.print(error_panel)
                raise typer.Exit(1)

    if script_type:
        if script_type not in SCRIPT_TYPE_CHOICES:
            console.print(
                f"[red]Error:[/red] Invalid script type '{script_type}'. Choose from: {', '.join(SCRIPT_TYPE_CHOICES.keys())}"
            )
            raise typer.Exit(1)
        selected_script = script_type
    else:
        default_script = "ps" if os.name == "nt" else "sh"

        if sys.stdin.isatty():
            selected_script = select_with_arrows(
                SCRIPT_TYPE_CHOICES,
                "Choose script type (or press Enter)",
                default_script,
            )
        else:
            selected_script = default_script

    console.print(f"[cyan]Selected AI assistant:[/cyan] {selected_ai}")
    console.print(f"[cyan]Selected script type:[/cyan] {selected_script}")

    tracker = StepTracker("Initialize NUAA Project")

    sys._specify_tracker_active = True  # type: ignore[attr-defined]

    tracker.add("precheck", "Check required tools")
    tracker.complete("precheck", "ok")
    tracker.add("ai-select", "Select AI assistant")
    tracker.complete("ai-select", f"{selected_ai}")
    tracker.add("script-select", "Select script type")
    tracker.complete("script-select", selected_script)
    for key, label in [
        ("fetch", "Fetch latest release"),
        ("download", "Download template"),
        ("extract", "Extract template"),
        ("zip-list", "Archive contents"),
        ("extracted-summary", "Extraction summary"),
        ("chmod", "Ensure scripts executable"),
        ("cleanup", "Cleanup"),
        ("git", "Initialize git repository"),
        ("final", "Finalize"),
    ]:
        tracker.add(key, label)

    # Track git error message outside Live context so it persists
    git_error_message = None

    with Live(tracker.render(), console=console, refresh_per_second=8, transient=True) as live:
        tracker.attach_refresh(lambda: live.update(tracker.render()))
        try:
            verify = not skip_tls
            local_ssl_context = ssl_context if verify else False

            with httpx.Client(verify=local_ssl_context) as local_client:
                download_and_extract_template(
                    project_path,
                    selected_ai,
                    selected_script,
                    here,
                    verbose=False,
                    tracker=tracker,
                    client=local_client,
                    debug=debug,
                    github_token=github_token,
                )

            ensure_executable_scripts(project_path, tracker=tracker)

            if not no_git:
                tracker.start("git")
                if is_git_repo(project_path):
                    tracker.complete("git", "existing repo detected")
                elif should_init_git:
                    success, error_msg = init_git_repo(project_path, quiet=True)
                    if success:
                        tracker.complete("git", "initialized")
                    else:
                        tracker.error("git", "init failed")
                        git_error_message = error_msg
                else:
                    tracker.skip("git", "git not available")
            else:
                tracker.skip("git", "--no-git flag")

            tracker.complete("final", "project ready")
        except Exception as e:
            tracker.error("final", str(e))
            console.print(Panel(f"Initialization failed: {e}", title="Failure", border_style="red"))
            if debug:
                _env_pairs = [
                    ("Python", sys.version.split()[0]),
                    ("Platform", sys.platform),
                    ("CWD", str(Path.cwd())),
                ]
                _label_width = max(len(k) for k, _ in _env_pairs)
                env_lines = [
                    f"{k.ljust(_label_width)} → [bright_black]{v}[/bright_black]"
                    for k, v in _env_pairs
                ]
                console.print(
                    Panel(
                        "\n".join(env_lines),
                        title="Debug Environment",
                        border_style="magenta",
                    )
                )
            if not here and project_path.exists():
                shutil.rmtree(project_path)
            raise typer.Exit(1)
        finally:
            pass

    console.print(tracker.render())
    console.print("\n[bold green]NUAA project workspace ready.[/bold green]")

    # Show git error details if initialization failed
    if git_error_message:
        console.print()
        git_error_panel = Panel(
            f"[yellow]Warning:[/yellow] Git repository initialization failed\n\n"
            f"{git_error_message}\n\n"
            f"[dim]You can initialize git manually later with:[/dim]\n"
            f"[cyan]cd {project_path if not here else '.'}[/cyan]\n"
            f"[cyan]git init[/cyan]\n"
            f"[cyan]git add .[/cyan]\n"
            f'[cyan]git commit -m "Initial commit"[/cyan]',
            title="[red]Git Initialization Failed[/red]",
            border_style="red",
            padding=(1, 2),
        )
        console.print(git_error_panel)

    # Agent folder security notice
    agent_config = AGENT_CONFIG.get(selected_ai)
    if agent_config:
        agent_folder = agent_config["folder"]
        security_notice = Panel(
            f"Some agents may store credentials, auth tokens, or other identifying and private artifacts in the agent folder within your project.\n"
            f"Consider adding [cyan]{agent_folder}[/cyan] (or parts of it) to [cyan].gitignore[/cyan] to prevent accidental credential leakage.",
            title="[yellow]Agent Folder Security[/yellow]",
            border_style="yellow",
            padding=(1, 2),
        )
        console.print()
        console.print(security_notice)

    steps_lines = []
    if not here:
        steps_lines.append(f"1. Go to the project folder: [cyan]cd {project_name}[/cyan]")
        step_num = 2
    else:
        steps_lines.append("1. You're already in the project directory!")
        step_num = 2

    # Add Codex-specific setup step if needed
    if selected_ai == "codex":
        codex_path = project_path / ".codex"
        quoted_path = shlex.quote(str(codex_path))
        if os.name == "nt":  # Windows
            cmd = f"setx CODEX_HOME {quoted_path}"
        else:  # Unix-like systems
            cmd = f"export CODEX_HOME={quoted_path}"

        steps_lines.append(
            f"{step_num}. Set [cyan]CODEX_HOME[/cyan] environment variable before running Codex: [cyan]{cmd}[/cyan]"
        )
        step_num += 1

    steps_lines.append(f"{step_num}. Start using slash commands with your AI agent:")

    steps_lines.append("   2.1 [cyan]/nuaa.design[/] - Create program designs with logic models")
    steps_lines.append("   2.2 [cyan]/nuaa.propose[/] - Generate funding proposals")
    steps_lines.append("   2.3 [cyan]/nuaa.measure[/] - Define impact measurement frameworks")
    steps_lines.append("   2.4 [cyan]/nuaa.document[/] - Document existing programs")
    steps_lines.append("   2.5 [cyan]/nuaa.refine[/] - Refine and improve outputs")

    steps_panel = Panel(
        "\n".join(steps_lines), title="Next Steps", border_style="cyan", padding=(1, 2)
    )
    console.print()
    console.print(steps_panel)

    enhancement_lines = [
        "Additional NUAA commands available [bright_black](comprehensive program management)[/bright_black]",
        "",
        f"○ [cyan]/nuaa.report[/] [bright_black](optional)[/bright_black] - Generate reports and presentations from program data",
        f"○ [cyan]/nuaa.refine[/] [bright_black](optional)[/bright_black] - Improve and iterate on existing documents",
        "",
    ]
    enhancements_panel = Panel(
        "\n".join(enhancement_lines),
        title="Enhancement Commands",
        border_style="cyan",
        padding=(1, 2),
    )
    console.print()
    console.print(enhancements_panel)


@app.command()
def check():
    """Check that all required tools are installed."""
    show_banner()
    console.print("[bold]Checking for installed tools...[/bold]\n")

    tracker = StepTracker("Check Available Tools")

    tracker.add("git", "Git version control")
    git_ok = check_tool("git", tracker=tracker)

    cli_agent_results: dict[str, bool] = {}
    has_ide_agent = False
    for agent_key, agent_config in AGENT_CONFIG.items():
        agent_name = agent_config["name"]
        requires_cli = agent_config["requires_cli"]

        tracker.add(agent_key, agent_name)

        if requires_cli:
            cli_agent_results[agent_key] = check_tool(agent_key, tracker=tracker)
        else:
            # IDE-based agent - skip CLI check and mark as optional
            tracker.skip(agent_key, "IDE-based, no CLI check")
            has_ide_agent = True

    # Check VS Code variants (not in agent config)
    tracker.add("code", "Visual Studio Code")
    code_ok = check_tool("code", tracker=tracker)

    tracker.add("code-insiders", "Visual Studio Code Insiders")
    code_insiders_ok = check_tool("code-insiders", tracker=tracker)

    console.print(tracker.render())

    console.print("\n[bold green]NUAA CLI is ready to use![/bold green]")

    if not git_ok:
        console.print("[dim]Tip: Install git for repository management[/dim]")

    if not any(cli_agent_results.values()):
        if has_ide_agent:
            console.print(
                "[dim]Tip: Install a CLI-based AI assistant if you need standalone workflows; IDE assistants are already supported.[/dim]"
            )
        else:
            console.print("[dim]Tip: Install an AI assistant for the best experience[/dim]")


@app.command()
def design(
    program_name: str = typer.Argument(..., help="Program name (used to derive feature folder)"),
    target_population: str = typer.Argument(..., help="Target population description"),
    duration: str = typer.Argument(..., help="Program duration (e.g., '6 months')"),
    here: bool = typer.Option(True, help="Create under ./nuaa (current project)"),
    feature: Optional[str] = typer.Option(
        None, help="Override feature slug (e.g., '001-custom-slug')"
    ),
    force: bool = typer.Option(False, help="Overwrite existing files if present"),
):
    """Create a new NUAA program design with logic model and impact framework scaffolds."""
    show_banner()
    # Determine feature directory
    if feature:
        # If full number provided, respect it; otherwise create next
        if re.match(r"^\d{3}-", feature):
            feature_dir = _ensure_nuaa_root() / feature
            feature_dir.mkdir(parents=True, exist_ok=True)
            num_str = feature[:3]
            slug = feature.split("-", 1)[1]
        else:
            # Treat as slug only; compute next number
            slug = _slugify(feature)
            feature_dir, num_str, _ = _next_feature_dir(slug)
    else:
        feature_dir, num_str, slug = _next_feature_dir(program_name)

    created = datetime.now().strftime("%Y-%m-%d")
    mapping = {
        "PROGRAM_NAME": program_name,
        "TARGET_POPULATION": target_population,
        "DURATION": duration,
        "DATE": created,
        "FEATURE_ID": num_str,
        "SLUG": slug,
    }

    # program-design.md
    try:
        pd_template = _load_template("program-design.md")
        pd_filled = _apply_replacements(pd_template, mapping)
        pd_meta = {
            "title": f"{program_name} - Program Design",
            "created": created,
            "feature": f"{num_str}-{slug}",
            "status": "draft",
        }
        pd_text = _prepend_metadata(pd_filled, pd_meta)
        dest = feature_dir / "program-design.md"
        if dest.exists() and not force:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
        else:
            _write_markdown(dest, pd_text)
            console.print(f"[green]Created:[/green] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create program-design.md:[/red] {e}")
        raise typer.Exit(1)

    # logic-model.md
    try:
        lm_template = _load_template("logic-model.md")
        lm_text = _prepend_metadata(
            _apply_replacements(lm_template, mapping),
            {"title": f"{program_name} - Logic Model", "feature": f"{num_str}-{slug}"},
        )
        dest = feature_dir / "logic-model.md"
        if not dest.exists() or force:
            _write_markdown(dest, lm_text)
            console.print(f"[green]Created:[/green] {dest}")
        else:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create logic-model.md:[/red] {e}")

    # impact-framework.md (skeleton from template)
    try:
        if_template = _load_template("impact-framework.md")
        if_text = _prepend_metadata(
            _apply_replacements(if_template, mapping),
            {
                "title": f"{program_name} - Impact Framework",
                "feature": f"{num_str}-{slug}",
            },
        )
        dest = feature_dir / "impact-framework.md"
        if not dest.exists() or force:
            _write_markdown(dest, if_text)
            console.print(f"[green]Created:[/green] {dest}")
        else:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create impact-framework.md:[/red] {e}")

    # Changelog bootstrap
    changelog = feature_dir / "CHANGELOG.md"
    if not changelog.exists():
        _write_markdown(
            changelog,
            f"# Changelog for {num_str}-{slug}\n\n- {_stamp()} - Initialized program design\n",
        )
        console.print(f"[green]Created:[/green] {changelog}")

    console.print(
        Panel(
            f"Feature ready: [cyan]{feature_dir}[/cyan]",
            title="Design Created",
            border_style="green",
        )
    )


@app.command()
def propose(
    program_name: str = typer.Argument(..., help="Program name (existing or new)"),
    funder: str = typer.Argument(..., help="Funder name"),
    amount: str = typer.Argument(..., help="Amount requested, e.g., $50000"),
    duration: str = typer.Argument(..., help="Duration e.g., '12 months'"),
    force: bool = typer.Option(False, help="Overwrite if proposal.md exists"),
):
    """Create a funding proposal from the template, linked to the program design."""
    show_banner()
    feature_dir = _find_feature_dir_by_program(program_name) or _next_feature_dir(program_name)[0]
    created = datetime.now().strftime("%Y-%m-%d")
    mapping = {
        "PROGRAM_NAME": program_name,
        "FUNDER": funder,
        "AMOUNT": amount,
        "DURATION": duration,
        "DATE": created,
    }
    try:
        template = _load_template("proposal.md")
        filled = _apply_replacements(template, mapping)
        meta = {
            "title": f"{program_name} - Proposal",
            "funder": funder,
            "amount": amount,
            "created": created,
        }
        text = _prepend_metadata(filled, meta)
        dest = feature_dir / "proposal.md"
        if dest.exists() and not force:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
        else:
            _write_markdown(dest, text)
            console.print(f"[green]Created:[/green] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create proposal.md:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def measure(
    program_name: str = typer.Argument(..., help="Program name (existing)"),
    evaluation_period: str = typer.Argument(..., help="Evaluation period"),
    budget: str = typer.Argument(..., help="Evaluation budget (e.g., $7000)"),
    force: bool = typer.Option(False, help="Overwrite if exists"),
):
    """Create or update the impact framework document from the template."""
    show_banner()
    feature_dir = _find_feature_dir_by_program(program_name) or _next_feature_dir(program_name)[0]
    mapping = {
        "PROGRAM_NAME": program_name,
        "EVALUATION_PERIOD": evaluation_period,
        "BUDGET": budget,
        "DATE": datetime.now().strftime("%Y-%m-%d"),
    }
    try:
        template = _load_template("impact-framework.md")
        text = _prepend_metadata(
            _apply_replacements(template, mapping),
            {"title": f"{program_name} - Impact Framework"},
        )
        dest = feature_dir / "impact-framework.md"
        if dest.exists() and not force:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
        else:
            _write_markdown(dest, text)
            console.print(f"[green]Created:[/green] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create impact-framework.md:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def document(
    program_name: str = typer.Argument(..., help="Existing program identifier/name"),
    force: bool = typer.Option(False, help="Overwrite if exists"),
):
    """Create an existing program analysis document (brownfield documentation)."""
    show_banner()
    feature_dir = _find_feature_dir_by_program(program_name) or _next_feature_dir(program_name)[0]
    mapping = {
        "PROGRAM_NAME": program_name,
        "DATE": datetime.now().strftime("%Y-%m-%d"),
    }
    try:
        template = _load_template("existing-program-analysis.md")
        text = _prepend_metadata(
            _apply_replacements(template, mapping),
            {"title": f"{program_name} - Existing Program Analysis"},
        )
        dest = feature_dir / "existing-program-analysis.md"
        if dest.exists() and not force:
            console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
        else:
            _write_markdown(dest, text)
            console.print(f"[green]Created:[/green] {dest}")
    except Exception as e:
        console.print(f"[red]Failed to create existing-program-analysis.md:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def report(
    program_name: str = typer.Argument(..., help="Program name (existing)"),
    report_type: str = typer.Option(
        "final",
        "--type",
        help="Report type: progress|mid-program|final|quarterly|annual",
    ),
    force: bool = typer.Option(False, help="Overwrite if exists"),
):
    """Generate a simple report scaffold referencing program artifacts."""
    show_banner()
    feature_dir = _find_feature_dir_by_program(program_name) or _next_feature_dir(program_name)[0]
    created = datetime.now().strftime("%Y-%m-%d")
    content = f"""# {program_name} - {report_type.title()} Report

Generated: {created}

This is a scaffold report. Populate the sections based on your impact framework and collected data.

## Overview

## Key Findings

## Progress Against Logic Model

## Equity Analysis

## Budget vs Actuals

## Lessons Learned and Recommendations

"""
    dest = feature_dir / "report.md"
    if dest.exists() and not force:
        console.print(f"[yellow]File exists, skipping:[/yellow] {dest}")
    else:
        _write_markdown(dest, content)
        console.print(f"[green]Created:[/green] {dest}")


@app.command()
def refine(
    program_name: str = typer.Argument(..., help="Program name (existing)"),
    note: str = typer.Option("Refinement applied", "--note", help="Changelog note to record"),
):
    """Record a refinement entry in the feature CHANGELOG.md."""
    show_banner()
    feature_dir = _find_feature_dir_by_program(program_name)
    if not feature_dir:
        console.print("[red]Could not find feature directory for program[/red]")
        raise typer.Exit(1)
    changelog = feature_dir / "CHANGELOG.md"
    entry = f"- {_stamp()} - {note}\n"
    if changelog.exists():
        with open(changelog, "a", encoding="utf-8") as f:
            f.write(entry)
    else:
        _write_markdown(changelog, f"# Changelog for {feature_dir.name}\n\n" + entry)
    console.print(f"[green]Updated:[/green] {changelog}")


@app.command()
def mission(
    set: Optional[str] = typer.Option(None, "--set", help="Set mission statement and create constitution"),
    edit: bool = typer.Option(False, "--edit", help="Edit constitution in default editor"),
    show: bool = typer.Option(False, "--show", help="Display current constitution"),
):
    """Create or manage the NUAA mission constitution."""
    show_banner()
    constitution_path = Path("memory/constitution.md")
    
    if show:
        # Display existing constitution
        if not constitution_path.exists():
            console.print("[yellow]No constitution found. Create one with --set[/yellow]")
            raise typer.Exit(1)
        content = constitution_path.read_text(encoding="utf-8")
        console.print(Panel(content, title="Mission Constitution", border_style="blue"))
    
    elif edit:
        # Open in default editor
        if not constitution_path.exists():
            console.print("[yellow]No constitution found. Create one first with --set[/yellow]")
            raise typer.Exit(1)
        typer.launch(str(constitution_path), locate=False)
        console.print("✓ Constitution updated. Run agent context update if needed.")
    
    elif set:
        # Create new constitution from template
        template_path = _find_templates_root() / "mission-constitution-template.md"
        if not template_path.exists():
            console.print("[red]Template not found. Check installation.[/red]")
            raise typer.Exit(1)
        
        # Copy template and populate
        constitution_path.parent.mkdir(parents=True, exist_ok=True)
        content = template_path.read_text(encoding="utf-8")
        
        # Replace core mission placeholder
        content = content.replace("[CORE_MISSION]", set)
        
        # Replace date placeholders
        today = datetime.now().strftime("%Y-%m-%d")
        next_year = datetime.now().replace(year=datetime.now().year + 1).strftime("%Y-%m-%d")
        content = content.replace("[RATIFICATION_DATE]", today)
        content = content.replace("[NEXT_REVIEW_DATE]", next_year)
        
        # Replace other placeholder sections with defaults
        # Lived Experience commitments
        content = content.replace("[LIVED_EXPERIENCE_COMMITMENT_1]", "People with lived experience lead program design, delivery, and evaluation")
        content = content.replace("[LIVED_EXPERIENCE_COMMITMENT_2]", "Peer workers are valued, supported, and fairly compensated for their expertise")
        content = content.replace("[LIVED_EXPERIENCE_COMMITMENT_3]", "Lived experience is recognized as equal to academic or professional expertise")
        
        # Harm Reduction commitments
        content = content.replace("[HARM_REDUCTION_COMMITMENT_1]", "Programs are grounded in evidence-based harm reduction principles")
        content = content.replace("[HARM_REDUCTION_COMMITMENT_2]", "People's choices about drug use are respected without judgment")
        content = content.replace("[HARM_REDUCTION_COMMITMENT_3]", "Support is offered without requiring abstinence or behavior change")
        
        # Cultural Safety commitments
        content = content.replace("[CULTURAL_SAFETY_COMMITMENT_1]", "Aboriginal and Torres Strait Islander peoples' cultural protocols are respected")
        content = content.replace("[CULTURAL_SAFETY_COMMITMENT_2]", "LGBTIQ+ inclusion is embedded in all programs")
        content = content.replace("[CULTURAL_SAFETY_COMMITMENT_3]", "Programs are accessible to culturally and linguistically diverse communities")
        
        # Data Ethics commitments
        content = content.replace("[DATA_ETHICS_COMMITMENT_1]", "Participants provide free and informed consent for data collection and use")
        content = content.replace("[DATA_ETHICS_COMMITMENT_2]", "Data security and privacy are prioritized in all systems")
        content = content.replace("[DATA_ETHICS_COMMITMENT_3]", "Community benefits from data use - never harmed by it")
        
        # Evidence requirements
        content = content.replace("[EVIDENCE_REQUIREMENT_1]", "All programs cite relevant harm reduction research and community evidence")
        content = content.replace("[EVIDENCE_REQUIREMENT_2]", "Community knowledge and lived experience are valued as evidence")
        content = content.replace("[EVIDENCE_REQUIREMENT_3]", "Programs adapt based on evaluation findings and community feedback")
        
        # Evaluation requirements
        content = content.replace("[EVALUATION_REQUIREMENT_1]", "Evaluation questions and methods are defined before program starts")
        content = content.replace("[EVALUATION_REQUIREMENT_2]", "People with lived experience participate in evaluation design and analysis")
        content = content.replace("[EVALUATION_REQUIREMENT_3]", "Evaluation findings are shared with community and contribute to harm reduction knowledge")
        
        # Budget requirements
        content = content.replace("[BUDGET_REQUIREMENT_1]", "Budgets reflect true costs including adequate peer worker compensation")
        content = content.replace("[BUDGET_REQUIREMENT_2]", "Financial sustainability is planned from program design phase")
        content = content.replace("[BUDGET_REQUIREMENT_3]", "Budget priorities align with organizational values (fair pay, cultural safety, community benefit)")
        
        # Accountability mechanisms
        content = content.replace("[ACCOUNTABILITY_MECHANISM_1]", "Programs are reviewed regularly by staff, management, and consumer advisory")
        content = content.replace("[ACCOUNTABILITY_MECHANISM_2]", "Community feedback is actively sought and incorporated")
        content = content.replace("[ACCOUNTABILITY_MECHANISM_3]", "Deviations from constitutional principles require explicit justification and approval")
        
        constitution_path.write_text(content, encoding="utf-8")
        
        console.print(f"✓ Mission constitution created at {constitution_path}")
        
        # Update agent context files
        update_script_bash = Path("scripts/bash/update-agent-context.sh")
        update_script_ps = Path("scripts/powershell/update-agent-context.ps1")
        
        script_run = False
        if sys.platform == "win32" and update_script_ps.exists():
            try:
                result = subprocess.run(
                    ["pwsh", "-File", str(update_script_ps)],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                if result.returncode == 0:
                    console.print("✓ Updated agent context files")
                    script_run = True
                else:
                    console.print(f"[yellow]⚠ Agent context update returned error: {result.stderr}[/yellow]")
            except Exception as e:
                console.print(f"[yellow]⚠ Could not run agent context update: {e}[/yellow]")
        elif update_script_bash.exists():
            try:
                result = subprocess.run(
                    ["bash", str(update_script_bash)],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                if result.returncode == 0:
                    console.print("✓ Updated agent context files")
                    script_run = True
                else:
                    console.print(f"[yellow]⚠ Agent context update returned error: {result.stderr}[/yellow]")
            except Exception as e:
                console.print(f"[yellow]⚠ Could not run agent context update: {e}[/yellow]")
        
        if not script_run:
            console.print("[yellow]⚠ Could not find update script. Manually run agent context update if needed.[/yellow]")
    
    else:
        console.print("Use --set, --edit, or --show")
        raise typer.Exit(1)


@app.command()
def version():
    """Display version and system information."""
    import platform
    import importlib.metadata

    show_banner()

    # Get CLI version from package metadata
    cli_version = "unknown"
    try:
        cli_version = importlib.metadata.version("nuaa-cli")
    except Exception:
        # Fallback: try reading from pyproject.toml if running from source
        try:
            import tomllib

            pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)
                    cli_version = data.get("project", {}).get("version", "unknown")
        except Exception:
            pass

    # Fetch latest NUAA release version (reporting only; does not affect template downloads)
    repo_owner = "zophiezlan"
    repo_name = "spec-driven-projects"
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    template_version = "unknown"
    release_date = "unknown"

    try:
        with httpx.Client(verify=ssl_context) as http_client:
            response = http_client.get(
                api_url,
                timeout=10,
                follow_redirects=True,
                headers=_github_auth_headers(),
            )
            if response.status_code == 200:
                release_data = response.json()
                template_version = release_data.get("tag_name", "unknown")
                # Remove 'v' prefix if present
                if template_version.startswith("v"):
                    template_version = template_version[1:]
                release_date = release_data.get("published_at", "unknown")
                if release_date != "unknown":
                    # Format the date nicely
                    try:
                        dt = datetime.fromisoformat(release_date.replace("Z", "+00:00"))
                        release_date = dt.strftime("%Y-%m-%d")
                    except Exception:
                        pass
    except Exception:
        pass

    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_column("Key", style="cyan", justify="right")
    info_table.add_column("Value", style="white")

    info_table.add_row("CLI Version", cli_version)
    info_table.add_row("Template Version", template_version)
    info_table.add_row("Released", release_date)
    info_table.add_row("", "")
    info_table.add_row("Python", platform.python_version())
    info_table.add_row("Platform", platform.system())
    info_table.add_row("Architecture", platform.machine())
    info_table.add_row("OS Version", platform.version())

    panel = Panel(
        info_table,
        title="[bold cyan]NUAA CLI Information[/bold cyan]",
        border_style="cyan",
        padding=(1, 2),
    )

    console.print(panel)
    console.print()


def main():
    app()


if __name__ == "__main__":
    main()
