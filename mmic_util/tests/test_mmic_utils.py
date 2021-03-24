"""
Unit and regression test for the mmic_util package.
"""

# Import package, test suite, and other packages as needed
import mmic_util
import pytest
import sys
import os

cwd = os.getcwd()

def test_mmic_util_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_util" in sys.modules


def test_mmic_util_ls():
    inp = mmic_util.models.CmdInput(engine="ls", args=[cwd, "-ltr"])
    return mmic_util.components.CmdComponent.compute(inp)

def test_mmic_util_grep():
    inp = mmic_util.models.CmdInput(engine="grep", args=["-r", "mmic", cwd])
    return mmic_util.components.CmdComponent.compute(inp)
