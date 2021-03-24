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

    def execute(
        self,
        inputs: Dict[str, Any],
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        env = os.environ.copy()
        scratch_directory = None

        if inputs.config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

            scratch_directory = config.scratch_directory

        exe_success, proc = execute(
            command=inputs.command,
            infiles=inputs.infiles,
            outfiles=inputs.outfiles,
            scratch_directory=scratch_directory,
            scratch_name=inputs.scratch_name,
            timeout=inputs.timeout,
            environment=env,
        )

        return exe_success, self.output()(**proc)
