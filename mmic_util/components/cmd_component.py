from qcengine.util import execute
from mmelemental.models.util.output import FileOutput
from mmic.components.blueprints import SpecificComponent
from typing import Any, Dict, List, Tuple, Optional, Union
from ..models import CmdOutput, CmdInput
import os

__all__ = ["CmdComponent"]


class CmdComponent(SpecificComponent):
    """ Cmd process: build_input() -> run() -> parse_output() -> [clean()] """

    @classmethod
    def input(cls):
        return CmdInput

    @classmethod
    def output(cls):
        return CmdOutput

    def clean(self, files: Union[List[FileOutput], FileOutput]):
        if isinstance(files, list):
            for file in files:
                file.remove()
        else:
            files.remove()

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        execute_input = self.build_input(inputs)
        exe_success, proc = self.run(execute_input)

        return exe_success, self.output()(**proc)

    def run(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        infiles = inputs["infiles"]
        outfiles = inputs["outfiles"]

        if extra_outfiles is not None:
            outfiles.extend(extra_outfiles)

        command = inputs["command"]
        if extra_commands is not None:
            command.extend(extra_commands)

        exe_success, proc = execute(
            command,
            infiles=infiles,
            outfiles=outfiles,
            scratch_directory=inputs["scratch_directory"],
            scratch_name=scratch_name,
            timeout=timeout,
            environment=inputs.get("environment", None),
        )

        return exe_success, proc

    def build_input(
        self,
        input_model: CmdInput,
        config: Optional["TaskConfig"] = None,
        template: Optional[str] = None,
    ) -> Dict[str, Any]:

        cmd = [input_model.engine]

        if input_model.kwargs is not None:
            for key, val in input_model.kwargs.items():
                cmd.extend([key, val])

        cmd.extend(input_model.flags)
        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        infiles = input_model.file_input.values() if input_model.file_input else None
        outfiles = input_model.file_output.items() if input_model.file_output else None

        return {
            "command": cmd,
            "infiles": infiles,
            "outfiles": outfiles,
            "scratch_directory": scratch_directory,
            "environment": env,
        }
