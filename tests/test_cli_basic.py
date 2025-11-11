import os
from pathlib import Path
from typer.testing import CliRunner

# Import the Typer app from the CLI module
from nuaa_cli.__init__ import app  # type: ignore


def test_version_runs():
    runner = CliRunner()
    # prints info; we only care it runs successfully
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0


def test_design_scaffolds(tmp_path: Path):
    # Create a temp project with nuaa-kit/templates copied from repo
    repo_root = Path(__file__).resolve().parents[1]
    templates_src = repo_root / "nuaa-kit" / "templates"
    assert templates_src.is_dir(), "templates not found; run tests from repository root"

    # Make a temp project root and symlink/copy templates tree
    project_root = tmp_path
    kit_dir = project_root / "nuaa-kit" / "templates"
    kit_dir.mkdir(parents=True, exist_ok=True)

    # Copy only the minimal templates used by design
    for name in [
        "program-design.md",
        "logic-model.md",
        "impact-framework.md",
    ]:
        src = templates_src / name
        dst = kit_dir / name
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    # Run the CLI from this directory
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        result = runner.invoke(
            app,
            [
                "design",
                "Peer Naloxone Distribution",
                "people at risk of opioid overdose",
                "12 months",
            ],
        )
        assert result.exit_code == 0, result.output

        # Verify outputs created
        nuaa_dir = project_root / "nuaa"
        assert nuaa_dir.is_dir()
        features = [p for p in nuaa_dir.iterdir() if p.is_dir()]
        assert features, "feature folder not created"
        feature = features[0]
        assert (feature / "program-design.md").is_file()
        assert (feature / "logic-model.md").is_file()
        assert (feature / "impact-framework.md").is_file()
        assert (feature / "CHANGELOG.md").is_file()
    finally:
        os.chdir(cwd)
