from .util import execute
from mmic.components import GenericComponent
from cmselemental.util.decorators import classproperty
from typing import Any, Dict, Tuple
from ..models import CmdOutput, CmdInput
import ntpath
import os

__all__ = ["CmdComponent"]


class CmdComponent(GenericComponent):
    @classproperty
    def input(cls):
        return CmdInput

    @classproperty
    def output(cls):
        return CmdOutput

    def execute(
        self,
        inputs: Dict[str, Any],
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input(**inputs)

        env = os.environ.copy()
        scratch_directory = inputs.scratch_directory

        if inputs.config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

            scratch_directory = config.scratch_directory

        infiles = {}
        if inputs.infiles:
            for fpath in inputs.infiles:
                flag = "r"
                fname = ntpath.basename(fpath)
                if inputs.as_binary:
                    if fname in inputs.as_binary:
                        flag = "rb"
                with open(fpath, flag) as fp:
                    infiles[fname] = fp.read()

        exe_success, proc = execute(
            command=inputs.command,
            as_binary=inputs.as_binary,
            infiles=infiles,
            outfiles=inputs.outfiles,
            outfiles_track=inputs.outfiles_track,
            scratch_directory=scratch_directory,
            scratch_name=inputs.scratch_name,
            scratch_messy=inputs.scratch_messy,
            timeout=inputs.timeout,
            environment=env,
        )

        if exe_success:
            if proc.get("stderr"):
                if inputs.raise_err:
                    raise RuntimeError(proc.get("stderr"))
            return exe_success, self.output(
                outfiles=proc.get("outfiles"),
                stdout=proc.get("stdout"),
                stderr=proc.get("stderr"),
                scratch_directory=proc.get("scratch_directory"),
            )
        else:
            raise RuntimeError(proc.get("stderr"))

    @classproperty
    def version(cls) -> str:
        """Returns distutils-style version string.

        Examples
        --------
        The string ">1.0, !=1.5.1, <2.0" implies any version after 1.0 and before 2.0
        is compatible, except 1.5.1

        Returns
        -------
        str
            Return a dist-utils valid version string.

        """
        return "0.0.0"
