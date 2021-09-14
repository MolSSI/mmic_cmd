mmic_cmd
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_cmd/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_cmd/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_cmd/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_cmd/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_cmd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_cmd/context:python)
[![docs](https://github.com/MolSSI/mmic_cmd/actions/workflows/doc.yaml/badge.svg)](https://molssi.github.io/mmic_cmd)

Package that provides command-line execution using qcengine.
A more thorough description to be followed in the near future ...

## CmdComponent
### General execution
```python
from mmic_cmd.components import CmdComponent

inp = {
    "command": [executable, "--arg", arg, "--out", ofile_name],
    "outfiles": [ofile_name],
}
outp = CmdComponent.compute(inp)

stdout, stderr = outp.stdout, outp.stderr
ofile_content = outp.outfiles[ofile_name]
```

### Specifying scratch dir & input files
```python
inp = {
    "command": [executable, "--in", ifile_name, "--out", ofile_name],
    "infiles": [ifile_path], # copy file to scratch tmp dir
    "outfiles": [ofile_name],
    "scratch_directory": path_to_scratch_dir,
}

outp = CmdComponent.compute(inp)

stdout, stderr = outp.stdout, outp.stderr
scratch_dir = outp.scratch_directory
```

### Tracking outfiles (no loading in memory)
By default, all files specified in `outfiles` are loaded in memory. To prevent that,
we pass `outfiles_track`, a list of output file names to track (and not load), to `compute`.
The file path, rather than its contents, are returned in `outfiles` for file names specified
in `outfiles_track`. To ensure these files persist (and do not get deleted) after execution,
we must set `scratch_mess=True` as well.

```python
inp = {
    "command": [executable, "--in", ifile_name, "--out", ofile_name],
    "infiles": [ifile_path], # copy file to scratch tmp dir
    "outfiles": [big_ofile_name, small_ofil_name],
    "outfiles_track": [big_ofile_name],
    "scratch_directory": path_to_scratch_dir,
    "scratch_messy": True, # do not remove scratch dir
}

outp = CmdComponent.compute(inp)

stdout, stderr = outp.stdout, outp.stderr
big_ofile_path = outp.outfiles[big_ofile_name] -> Path
small_ofile_cont = outp.outfiles[small_ofile_name] -> str
```


### Copyright

Copyright (c) 2021, MolSSI


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
