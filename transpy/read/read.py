"""The module contains the main function of the init file import process."""
"""The module contains the main function of the init file import process."""
import shlex



def read(file_):
    """The function reads the initialization file and returns a dictionary with parameters for the
    simulation.
    """
    check_presence_init(file_)

    dict_ = {'varnames': []}
    for line in open(file_).readlines():

        list_ = shlex.split(line)

        is_empty = (list_ == [])

        if not is_empty:
            is_keyword = list_[0].isupper()
        else:
            continue

        if is_keyword:
            keyword = list_[0]
            dict_[keyword] = {}
            continue

        process(list_, dict_, keyword)

    dict_ = auxiliary(dict_)

    return dict_