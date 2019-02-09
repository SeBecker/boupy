"""This module contains the random init file generating process that enables
us to produce random specifications for our upcoming test setup.
"""

import collections
import uuid

import numpy as np
import oyaml as yaml


def random_init(constr=None):
    """This function creates a random inititalization file."""
    if constr is not None:
        pass
    else:
        constr = {}
    if "PERIODS" in constr.keys():
        periods = constr["PERIODS"]
    else:
        periods = np.random.randint(2, 20)
    if "AGENTS" in constr.keys():
        agents = constr["AGENTS"]
    else:
        agents = np.random.randint(100, 5000)
    if "SEED" in constr.keys():
        seed = constr["SEED"]
    else:
        seed = np.random.randint(1000, 10000)
    if "SHARE" in constr.keys():
        share = constr["SHARE"]
    else:
        share = np.random.uniform(0.1, 0.8)
    if "FILE" in constr.keys():
        file = constr["FILE"]
    else:
        file = str(uuid.uuid4()).upper().replace("-", "")[0:8]

    init_dict = {"SIMULATION": {}, "PARAMS": {}, "DIST": {}}

    init_dict["SIMULATION"]["periods"] = periods
    init_dict["SIMULATION"]["agents"] = agents
    init_dict["SIMULATION"]["share"] = share
    init_dict["SIMULATION"]["seed"] = seed
    init_dict["SIMULATION"]["file"] = file

    init_dict["PARAMS"]["alpha"] = np.random.normal(1, 0.25)
    init_dict["PARAMS"]["theta"] = np.random.normal(0.1, 0.025)

    init_dict["DIST"]["beta"] = np.random.normal(0.75, 0.1)
    init_dict["DIST"]["mu"] = np.random.normal(0.5, 0.1)

    print_dict(init_dict)

    return init_dict


def print_dict(init_dict, file_name="test"):
    """This function prints the initialization dict to a *.yml file."""
    ordered_dict = collections.OrderedDict()
    order = ["SIMULATION", "PARAMS", "DIST"]
    for key_ in order:
        ordered_dict[key_] = init_dict[key_]

    with open("{}.boupy.yml".format(file_name), "w") as outfile:
        yaml.dump(ordered_dict, outfile, explicit_start=True, indent=4)
