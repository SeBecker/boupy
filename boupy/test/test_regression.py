"""The module includes an integration and a regression test for the simulation
process.
"""

import json

import numpy as np

from boupy.boupy_config import TEST_RESOURCES_DIR
from boupy.test.generate_init import random_init
from boupy.test.generate_init import print_dict
from boupy.simulate.simulate import simulate


def test1():
    """The test runs a loop to check the consistency of the random init file
     generating process and the following simulation.
    """
    for _ in range(1000):
        random_init()
        simulate("test.boupy.yml")


def test2():
    """This test runs a random selection of five regression tests from the our
    old regression testbattery.
    """
    fname = TEST_RESOURCES_DIR + "/regression_vault.boupy.json"
    tests = json.load(open(fname))
    random_choice = np.random.choice(range(len(tests)), 100)
    tests = [tests[i] for i in random_choice]

    for test in tests:
        stat, init_dict = test
        print_dict(init_dict)

        df = simulate("test.boupy.yml")
        stat_new = np.sum(df.sum())

        np.testing.assert_equal(stat, stat_new)
