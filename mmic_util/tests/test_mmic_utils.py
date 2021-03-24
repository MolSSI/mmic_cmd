"""
Unit and regression test for the mmic_util package.
"""

# Import package, test suite, and other packages as needed
import mmic_util
import pytest
import sys


def test_mmic_util_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_util" in sys.modules


inp = mmic_util.models.CmdInput(engine="ls", flags=["/", "-ltr"])
outp = mmic_util.components.CmdComponent.compute(inp)

print(outp.stdout)
