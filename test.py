from mmic_util.models import CmdInput
from mmic_util.components import CmdComponent
import os

pdb_file = os.path.abspath("../MMElemental/mmelemental/data/molecules/alanine.pdb")
outfiles = ["conf.gro", "topol.top", "posre.itp"]

inp = CmdInput(
    command=["gmx", "pdb2gmx", "-f", pdb_file, "-ff", "amber99", "-water", "none"],
    infiles=[pdb_file],
    # scratch_directory=path_to_scratch_dir,
    outfiles=outfiles,
    outfiles_load=False,
    # scratch_messy=True,
)
outp = CmdComponent.compute(inp)

conf, top, posre = (
    outp.outfiles["conf.gro"],
    outp.outfiles["topol.top"],
    outp.outfiles["posre.itp"],
)

print(outp.scratch_directory)
