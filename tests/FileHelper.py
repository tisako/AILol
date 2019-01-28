import inspect
import os


def get_current_dir():
    return os.path.dirname(os.path.abspath(inspect.stack()[1][1]))
