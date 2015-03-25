from checkio_referee import RefereeBase, covercodes, representations


import settings_env
from tests import TESTS



class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
        "python_2": covercodes.py_unwrap_args,
    }
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "python_2": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
