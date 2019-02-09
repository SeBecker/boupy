"""This module generates our regression test battery."""

import json
import os

import numpy as np

from boupy.boupy_config import TEST_RESOURCES_DIR
from boupy.test.generate_init import random_init
from boupy.simulate.simulate import simulate
from boupy.test.auxiliary import cleanup

NUM_TESTS = 1000

np.random.seed(1234235)
seeds = np.random.randint(0, 100000, size=NUM_TESTS)
directory = os.path.dirname(__file__)
file_dir = os.path.join(TEST_RESOURCES_DIR, "regression_vault.boupy.json")

tests = []
for seed in seeds:
    np.random.seed(seed)
    dict_ = random_init()
    df = simulate("test.boupy.yml")
    stat = np.sum(df.sum())
    tests += [(stat, dict_)]
json.dump(tests, open(file_dir, "w"))

cleanup()
