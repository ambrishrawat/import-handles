# import-handles
Boiler plate code setting handles to dataset and libraries

If the objective is to avoid playing around with PYTHONPATH, global configuration for data sets etc for your experiments, then this repository might be handy.

```python
'''main.py'''

from myrc import rc

from repo1 import *

if __name__=="__main":
    pass
```

Code structure:

* `myrc`
    * `__init__.py`
    * `handles`
        * `__init__.py`
        * `option_handle.py`

    
