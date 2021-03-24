mmic_util
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_util/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_util/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_util/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_util/branch/main)

Package that provides general-purpose utility components.
A more thorough description to be followed in the near future ...

## Snippet
### Pattern match with grep
```python
from mmic_util.models import CmdInput
from mmic_util.components import CmdComponent

inp = CmdInput(command=[pattern, "-r", path_to_files])
outp = CmdComponent.compute(inp)

stdout, stderr = outp.stdout, outp.stderr
```

### Pdb2Gmx with Gromacs
```python
pdb_file = abs_path_to_pdb_file

inp = CmdInput(
    command=["gmx", "pdb2gmx", "-f", pdb_file, "-ff", "amber99", "-water", "none"],
    outfiles=["conf.gro", "topol.top", "posre.itp"],
)
outp = CmdComponent.compute(inp)

conf, top, posre = (
    outp.outfiles["conf.gro"],
    outp.outfiles["topol.top"],
    outp.outfiles["posre.itp"],
)
```

### Specifying scratch dir
```python
inp = CmdInput(
    command=["gmx", "pdb2gmx", "-f", pdb_file, "-ff", "amber99", "-water", "none"],
    infiles=[pdb_file], # copy file to scratch tmp dir
    scratch_directory=path_to_scratch_dir,
    outfiles=outfiles,
    scratch_messy=True, # retain scratch tmp dir
)
outp = CmdComponent.compute(inp)

conf, top, posre = (
    outp.outfiles["conf.gro"],
    outp.outfiles["topol.top"],
    outp.outfiles["posre.itp"],
)
```

### Copyright

Copyright (c) 2021, Andrew Abi-Mansour


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
