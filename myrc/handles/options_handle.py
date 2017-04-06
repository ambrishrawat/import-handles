"""
handles

"""

import os
import sys

def execute(config):
   
    # Expand paths
    print('...expanding paths..')
    for name in config.keys():
        path = config[name]
        config[name] = os.path.abspath(os.path.expanduser(path))

    #Option - 1 : add to sys.path.insert(...)

    print('Option 1: adding to sys path')
    deeply_path = config['repo1']
    deeply_path = os.path.abspath(os.path.expanduser(deeply_path))
    sys.path.insert(1, deeply_path)

    #Option - 2 : add environment variables 
    print('Option 2: adding as an ENVIRONMENT VARIABLE')
    nltk_data = config['data1']
    nltk_data = os.path.abspath(os.path.expanduser(nltk_data))
    os.environ['DATA1'] = nltk_data
