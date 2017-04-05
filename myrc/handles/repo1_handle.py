"""deeply handle
"""

import os
import sys


def execute(rc):
    repo1_path = rc['repo1']
    repo1_path = os.path.abspath(os.path.expanduser(repo1_path))
    sys.path.insert(1, repo1_path)
