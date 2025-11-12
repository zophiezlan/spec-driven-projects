import os
from pathlib import Path
import re

from typer.testing import CliRunner

# Import the Typer app from the CLI module
from nuaa_cli.__init__ import app


def _copy_templates(templates_src: Path, kit_dir: Path, names: list[str]) -> None:
    """Copy specified templates from source to destination."""
    for name in names:
        src = templates_src / name
        dst = kit_dir / name
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


def _copy_scripts(scripts_src: Path, scripts_dir: Path, names: list[str]) -> None:
    """Copy specified scripts from source to destination."""
    for name in names:
        src = scripts_src / name
        dst = scripts_dir / name
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            # Make executable
            dst.chmod(0o755)


def test_specify_creates_initiative(tmp_path: Path):
    """Test that specify command creates an initiative with spec file."""
    repo_root = Path(__file__).resolve().parents[1]
    templates_src = repo_root / "nuaa-kit" / "templates"
    scripts_src = repo_root / "scripts" / "bash"
    
    assert templates_src.is_dir(), "templates not found; run tests from repository root"
    assert scripts_src.is_dir(), "scripts not found; run tests from repository root"
    
    # Setup temporary project
    project_root = tmp_path
    kit_dir = project_root / "nuaa-kit" / "templates"
    kit_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir = project_root / "scripts" / "bash"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy required template and script
    _copy_templates(templates_src, kit_dir, ["program-specification-template.md"])
    _copy_scripts(scripts_src, scripts_dir, ["create-new-initiative.sh"])
    
    # Run from project directory
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        result = runner.invoke(
            app,
            ["specify", "Peer naloxone distribution program for Western Sydney"],
        )
        
        # Check command succeeded
        assert result.exit_code == 0, f"Command failed: {result.output}"
        assert "Created initiative" in result.output
        
        # Verify directory structure
        initiatives_dir = project_root / "initiatives"
        assert initiatives_dir.is_dir(), "initiatives directory not created"
        
        # Find the created initiative
        initiative_dirs = list(initiatives_dir.glob("001-*"))
        assert len(initiative_dirs) == 1, f"Expected 1 initiative, found {len(initiative_dirs)}"
        
        initiative_dir = initiative_dirs[0]
        spec_file = initiative_dir / "spec.md"
        
        # Verify spec file exists and has content
        assert spec_file.is_file(), "spec.md not created"
        content = spec_file.read_text(encoding="utf-8")
        assert "Program Specification" in content
        assert "001-" in content  # Initiative number
        assert "[PLACEHOLDER:" in content  # Template placeholders present
        
    finally:
        os.chdir(cwd)


def test_clarify_resolves_markers(tmp_path: Path):
    """Test that clarify command finds and resolves [NEEDS CLARIFICATION] markers."""
    repo_root = Path(__file__).resolve().parents[1]
    
    # Setup temporary project
    project_root = tmp_path
    initiatives_dir = project_root / "initiatives" / "001-test-initiative"
    initiatives_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a spec with clarification markers
    spec_content = """---
title: "Test Program - Specification"
initiative: "001-test-initiative"
created: "2025-11-12"
status: "draft"
---

# Program Specification: Test Program

## Target Population

People who use drugs in regional NSW, particularly [NEEDS CLARIFICATION: Are we targeting people in treatment or harder-to-reach populations?]

Age range: [NEEDS CLARIFICATION: What age range? All adults (18+) or young adults (18-35)?]

## Duration

[NEEDS CLARIFICATION: Is this a pilot or ongoing service?]
"""
    spec_file = initiatives_dir / "spec.md"
    spec_file.write_text(spec_content, encoding="utf-8")
    
    # Run from project directory
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        
        # Simulate user input for the three questions
        result = runner.invoke(
            app,
            ["clarify", "001-test-initiative"],
            input="Harder-to-reach populations\nAll adults (18+)\nOngoing service\n"
        )
        
        # Check command succeeded
        assert result.exit_code == 0, f"Command failed: {result.output}"
        assert "Found 3 ambiguities" in result.output
        assert "Clarification Complete" in result.output
        
        # Verify markers were replaced
        updated_content = spec_file.read_text(encoding="utf-8")
        assert "[NEEDS CLARIFICATION:" not in updated_content, "Markers not removed"
        assert "Harder-to-reach populations" in updated_content
        assert "All adults (18+)" in updated_content
        assert "Ongoing service" in updated_content
        
    finally:
        os.chdir(cwd)


def test_clarify_no_markers(tmp_path: Path):
    """Test that clarify command handles specs with no markers gracefully."""
    project_root = tmp_path
    initiatives_dir = project_root / "initiatives" / "001-test-initiative"
    initiatives_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a spec without clarification markers
    spec_content = """---
title: "Test Program - Specification"
---

# Program Specification: Test Program

## Target Population

People who use drugs in regional NSW.

Age range: All adults (18+)
"""
    spec_file = initiatives_dir / "spec.md"
    spec_file.write_text(spec_content, encoding="utf-8")
    
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["clarify", "001-test-initiative"])
        
        assert result.exit_code == 0, f"Command failed: {result.output}"
        assert "No ambiguities to clarify" in result.output or "Specification Clear" in result.output
        
    finally:
        os.chdir(cwd)


def test_specify_auto_increment(tmp_path: Path):
    """Test that multiple specify commands create auto-incrementing initiatives."""
    repo_root = Path(__file__).resolve().parents[1]
    templates_src = repo_root / "nuaa-kit" / "templates"
    scripts_src = repo_root / "scripts" / "bash"
    
    # Setup project
    project_root = tmp_path
    kit_dir = project_root / "nuaa-kit" / "templates"
    kit_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir = project_root / "scripts" / "bash"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    _copy_templates(templates_src, kit_dir, ["program-specification-template.md"])
    _copy_scripts(scripts_src, scripts_dir, ["create-new-initiative.sh"])
    
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        
        # Create first initiative
        result1 = runner.invoke(app, ["specify", "First program"])
        assert result1.exit_code == 0
        assert "001-" in result1.output
        
        # Create second initiative
        result2 = runner.invoke(app, ["specify", "Second program"])
        assert result2.exit_code == 0
        assert "002-" in result2.output
        
        # Verify both exist
        initiatives_dir = project_root / "initiatives"
        initiative_dirs = sorted(initiatives_dir.glob("0*-*"))
        assert len(initiative_dirs) == 2
        assert initiative_dirs[0].name.startswith("001-")
        assert initiative_dirs[1].name.startswith("002-")
        
    finally:
        os.chdir(cwd)
