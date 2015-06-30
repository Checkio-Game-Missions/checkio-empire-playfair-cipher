from checkio_referee import RefereeBase, covercodes, representations, ENV_NAME


import settings_env
from tests import TESTS


def ext_str(data) -> str:
    """
    Extended str data conversion with quotes for strings.

    :param data: data for conversion
    :return: string representation
    """
    return '"{}"'.format(data) if isinstance(data, str) else str(data)


def representation(test, _):
    arguments = ", ".join(ext_str(d) for d in test["input"])
    return "{}({})".format(test["function_name"], arguments)


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_unwrap_args,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representation,
        ENV_NAME.JS_NODE: representation
    }
