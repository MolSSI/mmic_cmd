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
    args: Optional[List[str]] = Field(None, description="Positional command-line arguments or flags. "
        "Order is preserved. E.g. for the command: 'ls . -ltr', args=['.', '-ltr'].")
    kwargs: Optional[Dict[str, str]] = Field(
        None, description="Additional keyword arguments to pass to engine. Order is unimportant. "
        "E.g. for the command: 'exec --ifile path_to_file', kwargs={'--ifile': path_to_file}."
    )
