"""The module allows to run tests from inside the interpreter."""
import os

import pytest

from boupy.simulate.simulate import simulate
from boupy.boupy_config import PACKAGE_DIR
import boupy.boupy_config


def test():
    """The function allows to run the tests from inside the interpreter."""
    current_directory = os.getcwd()
    os.chdir(PACKAGE_DIR)
    pytest.main()
    os.chdir(current_directory)
