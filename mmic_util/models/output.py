from mmelemental.models import ProtoModel
from pydantic import Field
from typing import Optional, Dict
from pathlib import PosixPath
from subprocess import Popen

__all__ = ["CmdOutput"]


class CmdOutput(ProtoModel):
    stdout: str = Field(..., description="Standard output.")
    stderr: Optional[str] = Field(None, description="Standard error.")
    log: Optional[str] = Field(None, description="Logging output.")
    outfiles: Optional[Dict[str, str]] = Field(
        None,
        description="List of FileOutput objects. See the :class: ``mmelemental.models.FileOutput``.",
    )
    proc: Optional[Popen]
    scratch_directory: Optional[PosixPath]

    class Config(ProtoModel.Config):
        arbitrary_types_allowed = True
