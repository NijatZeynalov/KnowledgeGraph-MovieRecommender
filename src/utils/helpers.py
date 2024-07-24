
import os


def ensure_directory(path):
    """
    Ensure that the directory exists; if not, create it.

    :param path: Directory path to ensure.
    """
    if not os.path.exists(path):
        os.makedirs(path)
