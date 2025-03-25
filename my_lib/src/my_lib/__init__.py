VERSION = "1.0.0"
AUTHOR = "klamm"

from .my_math import my_sum
from .my_util import my_print 


# import subpackage
# from .subpackage import submodule1, submodule2


#import os
#import glob

## Auto-import all `.py` files in the package
#modules = glob.glob(os.path.dirname(__file__) + "/*.py")
#__all__ = [os.path.basename(f)[:-3] for f in modules if not f.endswith('__init__.py')]

print("mypackage has been loaded!")

