import inspect
import os


def get_current_dir(current_frame):
    return os.path.dirname(os.path.abspath(inspect.getfile(current_frame)))