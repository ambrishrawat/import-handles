"""Configuration utilities

Typically, do 'from config import config' to load a dictionary.

Behaviour:
1. Parse config.ini
2. Load section under profile variable
3. Execute handles
"""

import os
import configparser

from .handles import execute

__all__ = ['parser', 'rc']

config_file = os.path.join(os.path.dirname(__file__), 'rc.ini')

# Load config file
parser = configparser.ConfigParser()

with open(config_file, mode='rt') as f:
    parser.read_file(f)

# Generate config dictionary
rc = dict()
rc.update(parser['DEFAULT'])
profile = rc['profile'] = rc.get('profile', 'profile1')
if parser.has_section(profile):
    rc.update(parser[profile])

# Execute handles
execute(rc)
