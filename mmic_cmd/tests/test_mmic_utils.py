"""
Unit and regression test for the mmic_cmd package.
"""

# Import package, test suite, and other packages as needed
import mmic_cmd
import pytest
import sys
import os

cwd = os.getcwd()


def test_mmic_cmd_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_cmd" in sys.modules


def test_mmic_cmd_ls():
    inp = mmic_cmd.models.CmdInput(command=["ls", "-ltr", cwd])
    return mmic_cmd.components.CmdComponent.compute(inp)


def test_mmic_cmd_grep():
    inp = mmic_cmd.models.CmdInput(command=["grep", "-r", "mmic", cwd])
    return mmic_cmd.components.CmdComponent.compute(inp)
