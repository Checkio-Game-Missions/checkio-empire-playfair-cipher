from checkio_referee import RefereeBase, covercodes, representations


import settings_env
from tests import TESTS


def ext_str(data) -> str:
    """
    Extended str data conversion with quotes for strings.

    :param data: data for conversion
    :return: string representation
    """
    return '"{}"'.format(data) if isinstance(data, str) else str(data)


def py_repr(test, _):
    arguments = ", ".join(ext_str(d) for d in test["input"])
    return "{}({})".format(test["function_name"], arguments)


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
        "python_2": covercodes.py_unwrap_args,
    }
    CALLED_REPRESENTATIONS = {
        "python_3": py_repr,
    }
