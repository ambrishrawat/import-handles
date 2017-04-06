# import-handles

Boiler plate code setting handles to dataset and libraries

If the objective is to avoid playing around with PYTHONPATH, global configuration for data sets etc for your experiments, then this repository might be handy.

## Usage

```python
'''main.py'''

from myrc import rc

from mylib import *
from mydata import MYDATA_PROPERTIES

if __name__=="__main":
    pass

```

## Code Structure:

* `myrc`
    * `__init__.py`
    * `rc.ini`
    * `handles`
        * `__init__.py`
        * `option_handle.py`

    
