"""The module provides unit tests for different aspects of the simulation process."""

import numpy as np

from boupy.test.generate_init import random_init


def test1():
    """This test ensures that the dicts obtained by the random init generating
    process.
    """

    init_dict = random_init()

    np.testing.assert_equal(["SIMULATION", "PARAMS", "DIST"], list(init_dict.keys()))
