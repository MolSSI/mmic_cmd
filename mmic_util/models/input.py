from mmelemental.models import ProtoModel
from pydantic import Field
from typing import Optional, List, Dict

__all__ = ["CmdInput"]


class CmdInput(ProtoModel):
    """ Input schema for qcengine.execute """

    command: List[str] = Field(..., description=".")
    infiles: List[str] = Field(
        None,
        description="Input files (abs paths) to be written in scratch dir. May be {}.",
    )
    outfiles: Optional[List[str]] = Field(
        None,
        description="Output file name(s).",
    )
    outfiles_load: Optional[bool] = Field(
        False,
        description="If set to True, output files are loaded in memory. Otherwise, the posix paths "
        "are returned instead (default).",
    )
    as_binary: Optional[List[str]] = Field(
        None, description="Keys of `infiles` or `outfiles` to be treated as bytes."
    )
    scratch_name: Optional[str] = Field(
        None, description="Passed to temporary_directory."
    )
    scratch_directory: Optional[str] = Field(
        None, description="Passed to temporary_directory."
    )
    scratch_suffix: Optional[str] = Field(
        None, description="Passed to temporary_directory."
    )
    scratch_messy: bool = Field(False, description="Passed to temporary_directory")
    scratch_exist_ok: bool = Field(False, description="Passed to temporary_directory.")
    blocking_files: Optional[List[str]] = Field(
        None, description="Files which should stop execution if present beforehand."
    )
    timeout: Optional[int] = Field(
        None, description="Stop the process after n seconds."
    )
    interupt_after: Optional[int] = Field(
        None, description="Interupt the process (not hard kill) after n seconds."
    )
    environment: Optional[Dict[str, str]] = Field(
        None, description="The environment to run in."
    )
    shell: Optional[bool] = Field(False, description="Run command through the shell.")
    exit_code: Optional[int] = Field(
        0, description="The exit code above which the process is considered failure."
    )
    config: Optional["TaskConfig"] = Field(
        None,
        description="Config class for executing tasks. See :class: ``mmic.components.base.config.TaskConfig``.",
    )
