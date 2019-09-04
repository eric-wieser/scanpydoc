import warnings
from typing import Dict, Any

from sphinx.application import Sphinx
from sphinx.domains.python import PyTypedField

from . import _setup_sig, metadata


warnings.warn(
    "The functionality that used to be her is default as of Sphinx 2.0",
    DeprecationWarning,
)

DLTypedField = PyTypedField


@_setup_sig
def setup(app: Sphinx) -> Dict[str, Any]:
    return metadata
