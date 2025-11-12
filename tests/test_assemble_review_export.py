import os
from pathlib import Path
from typer.testing import CliRunner

from nuaa_cli.__init__ import app


def test_assemble_command_help():
    """Test that assemble command help works."""
    runner = CliRunner()
    result = runner.invoke(app, ["assemble", "--help"])
    assert result.exit_code == 0
    assert "Assemble validated sections" in result.output


def test_review_command_help():
    """Test that review command help works."""
    runner = CliRunner()
    result = runner.invoke(app, ["review", "--help"])
    assert result.exit_code == 0
    assert "Manage document review process" in result.output


def test_export_command_help():
    """Test that export command help works."""
    runner = CliRunner()
    result = runner.invoke(app, ["export", "--help"])
    assert result.exit_code == 0
    assert "Export assembled document" in result.output


def test_assemble_no_initiatives(tmp_path: Path):
    """Test assemble command with no initiatives directory."""
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["assemble"])
        assert result.exit_code == 1
        assert "No initiatives directory found" in result.output
    finally:
        os.chdir(cwd)


def test_review_no_initiatives(tmp_path: Path):
    """Test review command with no initiatives directory."""
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["review", "--action", "start"])
        assert result.exit_code == 1
        assert "No initiatives directory found" in result.output
    finally:
        os.chdir(cwd)


def test_export_no_script(tmp_path: Path):
    """Test export command when export script is missing."""
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["export"])
        assert result.exit_code == 1
        assert "Export script not found" in result.output
    finally:
        os.chdir(cwd)


def test_assemble_with_initiative_directory(tmp_path: Path):
    """Test assemble command when initiative exists but no plan."""
    project_root = tmp_path
    initiatives_dir = project_root / "initiatives" / "001-test"
    initiatives_dir.mkdir(parents=True, exist_ok=True)
    
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["assemble", "001-test"])
        assert result.exit_code == 1
        assert "Plan not found" in result.output
    finally:
        os.chdir(cwd)


def test_assemble_success_message(tmp_path: Path):
    """Test assemble command displays success message when plan exists."""
    project_root = tmp_path
    initiatives_dir = project_root / "initiatives" / "001-test"
    initiatives_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a minimal plan.md
    plan_file = initiatives_dir / "plan.md"
    plan_file.write_text("# Document Plan\n\nTest plan", encoding="utf-8")
    
    cwd = os.getcwd()
    os.chdir(project_root)
    try:
        runner = CliRunner()
        result = runner.invoke(app, ["assemble", "001-test"])
        assert result.exit_code == 0
        assert "Ready to Assemble" in result.output
        assert "AI will:" in result.output
        assert "/nuaa.assemble" in result.output
    finally:
        os.chdir(cwd)


def test_review_actions():
    """Test that all review actions are valid."""
    runner = CliRunner()
    
    # Valid actions should show in help
    result = runner.invoke(app, ["review", "--help"])
    assert result.exit_code == 0
    assert "start" in result.output
    assert "add-feedback" in result.output
    assert "summarize" in result.output
    assert "plan-revisions" in result.output
    assert "complete" in result.output
