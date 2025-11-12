"""Tests for Phase 3: Section Drafting and Revision commands"""

import os
import tempfile
from pathlib import Path
from typer.testing import CliRunner
from nuaa_cli import app

runner = CliRunner()


def test_draft_command_no_initiatives():
    """Test draft command with no initiatives directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section"])
            assert result.exit_code == 1
            assert "No initiatives directory found" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_no_plan():
    """Test draft command when plan doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory but no plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section"])
            assert result.exit_code == 1
            assert "Plan not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_section_not_in_plan():
    """Test draft command when section doesn't exist in plan"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Test Plan\n\n### Section 1: Other Section\n**Status**: Not Started")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section"])
            assert result.exit_code == 1
            assert "not found in plan" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_no_script():
    """Test draft command when script doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan that includes the section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Test Plan\n\n### Section 1: Test Section\n**Status**: Not Started")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section"])
            assert result.exit_code == 1
            assert "Script not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_resolve_no_section():
    """Test draft --resolve when section doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Test Plan\n\n### Section 1: Test Section\n**Status**: Not Started")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section", "--resolve"])
            assert result.exit_code == 1
            assert "Section draft not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_resolve_no_placeholders():
    """Test draft --resolve when section has no placeholders"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan and section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Test Plan\n\n### Section 1: Test Section\n**Status**: Not Started")
        
        sections_dir = initiatives_dir / "sections"
        sections_dir.mkdir()
        section_file = sections_dir / "test-section.md"
        section_file.write_text("# Test Section\n\nContent with no placeholders")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section", "--resolve"])
            assert result.exit_code == 0
            assert "No placeholders found" in result.stdout
        finally:
            os.chdir(cwd)


def test_draft_command_resolve_with_placeholders():
    """Test draft --resolve when section has placeholders"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan and section containing placeholders
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Test Plan\n\n### Section 1: Test Section\n**Status**: Not Started")
        
        sections_dir = initiatives_dir / "sections"
        sections_dir.mkdir()
        section_file = sections_dir / "test-section.md"
        section_file.write_text(
            "# Test Section\n\n[PLACEHOLDER: What is the budget?]\n\nSome content"
        )
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["draft", "Test Section", "--resolve"])
            assert result.exit_code == 0
            assert "Resolve Placeholders" in result.stdout
            assert (
                "Placeholders: 1" in result.stdout or 
                "Placeholders:\x1b[0m \x1b[93m1" in result.stdout
            )
        finally:
            os.chdir(cwd)


def test_revise_command_no_initiatives():
    """Test revise command with no initiatives directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["revise", "Test Section"])
            assert result.exit_code == 1
            assert "No initiatives directory found" in result.stdout
        finally:
            os.chdir(cwd)


def test_revise_command_section_not_exist():
    """Test revise command when section doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory but no section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["revise", "Test Section"])
            assert result.exit_code == 1
            assert "Section not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_revise_command_invalid_type():
    """Test revise command with invalid revision type"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        sections_dir = initiatives_dir / "sections"
        sections_dir.mkdir()
        section_file = sections_dir / "test-section.md"
        section_file.write_text("# Test Section\n\nContent")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["revise", "Test Section", "--type", "invalid"])
            assert result.exit_code == 1
            assert "Invalid revision type" in result.stdout
        finally:
            os.chdir(cwd)


def test_revise_command_valid_types():
    """Test revise command with all valid revision types"""
    valid_types = ["placeholder", "feedback", "consistency", "enhancement"]
    
    for revision_type in valid_types:
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create initiatives directory with section
            initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
            initiatives_dir.mkdir(parents=True)
            sections_dir = initiatives_dir / "sections"
            sections_dir.mkdir()
            section_file = sections_dir / "test-section.md"
            section_file.write_text("# Test Section\n\nContent")
            
            cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                result = runner.invoke(app, ["revise", "Test Section", "--type", revision_type])
                assert result.exit_code == 0
                assert "Ready to Revise" in result.stdout
                assert revision_type in result.stdout
            finally:
                os.chdir(cwd)


def test_revise_command_feedback_without_feedback_arg():
    """Test revise command with feedback type but no feedback argument"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        sections_dir = initiatives_dir / "sections"
        sections_dir.mkdir()
        section_file = sections_dir / "test-section.md"
        section_file.write_text("# Test Section\n\nContent")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["revise", "Test Section", "--type", "feedback"])
            assert result.exit_code == 0
            assert "No feedback provided" in result.stdout
        finally:
            os.chdir(cwd)


def test_revise_command_with_feedback():
    """Test revise command with feedback type and feedback argument"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with section
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        sections_dir = initiatives_dir / "sections"
        sections_dir.mkdir()
        section_file = sections_dir / "test-section.md"
        section_file.write_text("# Test Section\n\nContent")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(
                app, 
                ["revise", "Test Section", "--type", "feedback", "--feedback", "Add more details"]
            )
            assert result.exit_code == 0
            assert "Ready to Revise" in result.stdout
            assert "Add more details" in result.stdout
        finally:
            os.chdir(cwd)
