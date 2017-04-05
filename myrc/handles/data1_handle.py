"""data1 config handle
"""

import os


def execute(config):
    data1 = config['data1']
    data1 = os.path.abspath(os.path.expanduser(data1))
    os.environ['DATA1'] = data1
