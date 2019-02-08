"""This module provides some capabilities to check the integrity of the package."""
import os

import numpy as np

from grmpy.check.custom_exceptions import UserError

def check_consistency(init_dict):
    """This function performs some basic checks regarding the integrity of the user's request.
    There should be no uncontrolled terminations of the package once these checks are passed.
    """
    # Distribute details
    agents = init_dict["SIMULATION"]["agents"]
    periods = init_dict["SIMULATION"]["periods"]
    share = init_dict["SIMULATION"]["share"]

    # This are just two example for a whole host of tests.
    for key in [agents, periods]:
        if key <= 0:
            msg = "The specified number of {} needs to be larger than zero.".format(key)
            raise UserError(msg)
    if (share <= 0) | (share > 0.9):
            msg = "The specified share of treated individuals have to be large than 0.0 and smaller than 0.9.".format(key)
            raise UserError(msg)


        
def check_presence_init(fname):
    """This function checks whether the model initialization file does in fact exist."""
    if not os.path.isfile(fname):
        msg = "{}: There is no such file or directory.".format(fname)
        raise UserError(msg)
