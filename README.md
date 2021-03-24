mmic_util
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_util/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_util/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_util/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_util/branch/main)

Package that provides general-purpose utility components.
A more thorough description to be followed in the near future ...

## Snippet
```python
from mmic_util.models import CmdInput
from mmic_util.components import CmdComponent

inp = CmdInput(engine="grep", args=["-r", pattern, path_to_file])
outp = CmdComponent.compute(inp)

stdout, stderr = outp.stdout, outp.stderr
```

### Copyright

Copyright (c) 2021, Andrew Abi-Mansour


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
