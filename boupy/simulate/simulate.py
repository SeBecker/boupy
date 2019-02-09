"""This function contains the simulation process"""

import numpy as np

from boupy.simulate.simulate_auxiliary import simulate_outcomes
from boupy.simulate.simulate_auxiliary import create_dataframe
from boupy.simulate.simulate_auxiliary import switching
from boupy.simulate.simulate_auxiliary import baseline
from boupy.check.check import check_presence_init
from boupy.check.check import check_consistency
from boupy.read.read import read


def simulate(init_file):
    """This function simulates a dataframe accoridng to a pre-specified
     paramterization.
     """
    # Check if the specified init file exists
    check_presence_init(init_file)

    # Import Specifications and check for consistency
    init_dict = read(init_file)
    check_consistency(init_dict)

    np.random.seed(init_dict["SIMULATION"]["seed"])

    # Distribute parameters
    agents = init_dict["SIMULATION"]["agents"]
    share = init_dict["SIMULATION"]["share"]
    periods = init_dict["SIMULATION"]["periods"]
    alpha, theta = init_dict["PARAMS"]["alpha"], init_dict["PARAMS"]["theta"]
    mu, beta = init_dict["DIST"]["mu"], init_dict["DIST"]["beta"]

    # Simulate data
    base = baseline(agents, mu, beta, share)
    data = switching(periods, base, alpha, theta, False)
    data = simulate_outcomes(data)

    # Convert numpy object in pandas dataframe and save it as a pickle object
    df = create_dataframe(data, periods)
    df.to_pickle(init_dict["SIMULATION"]["file"] + ".boupy.pkl")

    return df
