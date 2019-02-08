"""The module contains the function of the init file import process."""
import yaml


def read(file):
    """This function processes the initialization file so that it can
    be used for simulation purposes.
    """

    # Check if there is a init file with the specified filename

    # Load the initialization file
    with open(file) as y:
        init_dict = yaml.load(y)

    # Create auxiliary section
    init_dict["AUX"] = {}
    init_dict["AUX"]["params"] = [
        init_dict["PARAMS"]["alpha"]
        + init_dict["PARAMS"]["theta"]
        + init_dict["DIST"]["mu"]
        + init_dict["DIST"]["beta"]
    ]

    return init_dict
