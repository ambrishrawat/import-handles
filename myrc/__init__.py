"""
rc utilities

Typically, do 'from nyrc import rc' to load a dictionary.

Actions:
1. parse rc.ini
2. load section under profile variable
3. execute handles
"""

import os
import configparser

from .handles import execute

# things to export from this module basically
# from myrc import parser
# from myrc import rc
__all__ = ['parser', 'rc']

config_file = os.path.join(os.path.dirname(__file__), 'rc.ini')

# Load config file
parser = configparser.ConfigParser()

with open(config_file, mode='rt') as f:
    parser.read_file(f)

# Generate config dictionary
rc = dict()
rc.update(parser['DEFAULT'])

# default behaviour - I have set profile1 as default wlog
profile = rc['profile'] = rc.get('profile', 'profile1')

if parser.has_section(profile):
    rc.update(parser[profile])

# Execute handles (executes handles as specified in handles/__init__.py
execute(rc)
