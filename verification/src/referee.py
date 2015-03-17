from checkio_referee import RefereeBase, covercodes, representations

import settings
import settings_env
from tests import TESTS



class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
        "python_2": covercodes.py_unwrap_args,
    }
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "python_2": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }