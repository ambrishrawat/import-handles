"""
handles
"""

import importlib


__all__ = ['execute']

modules = [
    'options_handle', 
    'repo1_handle', 
    'data1_handle'
]


def execute(config):
    for m in modules:
        mod = importlib.import_module('.{}'.format(m), __name__)
        mod.execute(config)
