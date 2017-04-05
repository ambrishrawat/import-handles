"""tf data handle
"""

import os
from ... import data


def execute(config):
    for name in config.keys():
        path = config[name]
        config[name] = os.path.abspath(os.path.expanduser(path))
