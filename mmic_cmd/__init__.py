"""
mmic_cmd
A short description of the project.
"""

# Add imports here
from .components import *
from .models import *
from . import models
from . import components

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
