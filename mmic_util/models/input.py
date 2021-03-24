from mmelemental.models import ProcInput, FileOutput
from pydantic import Field
from typing import Optional, List, Dict

__all__ = ["CmdInput"]


class CmdInput(ProcInput):
    file_input: List[str] = Field(
        None,
        description="Input file path(s) or name(s).",
    )
    file_output: Optional[List[str]] = Field(
        None,
        description="Output file path(s) or name(s).",
    )
    flags: Optional[List[str]] = Field(None, description="List of command-line flags.")
