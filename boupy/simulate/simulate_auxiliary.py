"""This module includes auxiliary functions for the simulation process."""

import pandas as pd
import numpy as np


def baseline(agents, mu, beta, share):
    """This function creates some baseline data."""
    # Create an empty array and determine the treated individuals
    treatment = np.zeros(agents)
    treatment[: int(agents * share)] = 1.0

    # Simulate and assign heterogeneity parameter
    heterogeneity = np.random.gamma(mu, beta, agents)

    # Combine both Arrays
    baseline = np.vstack([treatment, heterogeneity])

    return baseline


def switching(periods, baseline, alpha, theta, test=False):
    """The function distibutes calculates the probabilities for
    which every individual leaves the sample in each period.
    """
    # Distribute parameters
    agents = baseline.shape[1]
    gamma = baseline[1]
    deltam = 1 / (periods + 1)

    # Calculate switching probability for each individual for each time period
    prob = np.ones((periods, agents))

    if test is True:
        prob = prob * 0.05
    else:
        aux = baseline[0] * theta
        for period in range(periods):
            prob[period, :] = deltam * gamma * np.exp(alpha * period) * np.exp(aux)

    # Adjust probability matrix
    prob[prob > 1] = 1

    # Combine arrays
    data = np.vstack([baseline, prob])

    return data


def simulate_outcomes(data):
    """This function calculates the transitions for every individual in each period."""
    # Distribute Parameters
    periods = data.shape[0] - 2
    prob = data[2:].copy()

    # Determine which individual switches in which period
    transitions = np.random.binomial(1, prob, (periods, data.shape[1]))
    indicator = np.zeros((periods, data.shape[1]))

    # Create transition and indicator variables
    for period in range(periods - 1):
        transitions[period + 1 :, :] = (
            transitions[period + 1 :, :] - transitions[period, :]
        )
    transitions[transitions < 0] = 0

    for period in range(period):
        indicator[period + 1, :] = indicator[period, :] + transitions[period, :]

    # Combine Arrays
    data = np.vstack([np.vstack([data, transitions]), indicator])

    return data


def provide_renamedict(data, periods):
    """This function provides the rename dictionary based on the model
    specifications.
    """

    rename_dict = {0: "Treatment", 1: "Heterogeneity"}
    for col in range(data.shape[0] - (periods + 2)):
        if col < periods:
            rename_dict[col + periods + 2] = "Transition_{}".format(col)
        else:
            rename_dict[col + periods + 2] = "Indicator_{}".format(col - periods)

    return rename_dict


def create_dataframe(data, periods):
    """This function processes the simulated data into a pandas datframe
    object.
    """

    dataframe = pd.DataFrame(data.T)

    rename_dict = provide_renamedict(data, periods)

    dataframe = dataframe.rename(index=str, columns=rename_dict)

    # Drop probability matrix from data
    drop = [col for col in dataframe.columns.values if isinstance(col, int)]
    dataframe = dataframe.drop(drop, axis=1)

    return dataframe
