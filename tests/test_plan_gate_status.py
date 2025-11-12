"""Tests for Phase 2: Planning and Quality Gates commands"""

import os
import tempfile
import shutil
from pathlib import Path
from typer.testing import CliRunner
from nuaa_cli import app

runner = CliRunner()


def test_plan_command_no_initiatives():
    """Test plan command with no initiatives directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["plan"])
            assert result.exit_code == 1
            assert "No initiatives directory found" in result.stdout
        finally:
            os.chdir(cwd)


def test_plan_command_no_spec():
    """Test plan command when spec doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory but no spec
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["plan"])
            assert result.exit_code == 1
            assert "Specification not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_plan_command_with_spec():
    """Test plan command with valid spec file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with spec
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        spec_file = initiatives_dir / "spec.md"
        spec_file.write_text("# Test Spec\n\nSome content")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["plan"])
            assert result.exit_code == 0
            assert "Ready to Plan" in result.stdout
            assert "/nuaa.plan" in result.stdout
        finally:
            os.chdir(cwd)


def test_plan_command_with_clarifications():
    """Test plan command warns about unresolved clarifications"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create spec with clarification markers
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        spec_file = initiatives_dir / "spec.md"
        spec_file.write_text("# Test Spec\n\n[NEEDS CLARIFICATION: What is the target?]")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            # Answer "no" to continue anyway
            result = runner.invoke(app, ["plan"], input="n\n")
            assert result.exit_code == 0
            assert "unresolved clarifications" in result.stdout
        finally:
            os.chdir(cwd)


def test_gate_check_command_no_script():
    """Test gate-check command when script doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["gate-check", "Test Section"])
            assert result.exit_code == 1
            assert "Script not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_status_command_no_initiatives():
    """Test status command with no initiatives directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["status"])
            assert result.exit_code == 1
            assert "No initiatives directory found" in result.stdout
        finally:
            os.chdir(cwd)


def test_status_command_no_plan():
    """Test status command when plan doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory but no plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["status"])
            assert result.exit_code == 1
            assert "Plan not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_status_command_with_plan():
    """Test status command with valid plan file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Document Plan\n\nSome content")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["status"])
            assert result.exit_code == 0
            assert "Status Check Ready" in result.stdout
            assert "/nuaa.status" in result.stdout
        finally:
            os.chdir(cwd)


def test_plan_command_with_explicit_initiative():
    """Test plan command with explicit initiative argument"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple initiatives
        for i in range(1, 3):
            initiatives_dir = Path(tmpdir) / "initiatives" / f"00{i}-test"
            initiatives_dir.mkdir(parents=True)
            spec_file = initiatives_dir / "spec.md"
            spec_file.write_text(f"# Test Spec {i}\n\nSome content")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            # Test with explicit initiative
            result = runner.invoke(app, ["plan", "002-test"])
            assert result.exit_code == 0
            assert "002-test" in result.stdout
        finally:
            os.chdir(cwd)


def test_plan_command_with_type_option():
    """Test plan command with --type option"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with spec
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        spec_file = initiatives_dir / "spec.md"
        spec_file.write_text("# Test Spec\n\nSome content")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["plan", "--type", "proposal"])
            assert result.exit_code == 0
            assert "proposal" in result.stdout
        finally:
            os.chdir(cwd)


def test_gate_check_command_with_initiative_option():
    """Test gate-check command with --initiative option"""
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(
                app, 
                ["gate-check", "Test Section", "--initiative", "001-test"]
            )
            # Will fail due to missing script, but check args are accepted
            assert result.exit_code == 1
            assert "Script not found" in result.stdout
        finally:
            os.chdir(cwd)


def test_status_command_with_explicit_initiative():
    """Test status command with explicit initiative argument"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create initiatives directory with plan
        initiatives_dir = Path(tmpdir) / "initiatives" / "001-test"
        initiatives_dir.mkdir(parents=True)
        plan_file = initiatives_dir / "plan.md"
        plan_file.write_text("# Document Plan\n\nSome content")
        
        cwd = os.getcwd()
        os.chdir(tmpdir)
        try:
            result = runner.invoke(app, ["status", "001-test"])
            assert result.exit_code == 0
            assert "001-test" in result.stdout
        finally:
            os.chdir(cwd)

