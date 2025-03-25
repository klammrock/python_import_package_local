#import sys
#sys.path.append("../my_lib/src")


#PYTHONPATH="../my_lib/src" python src/my_main_app/main.py


# not works
#import importlib.util
#module_name = "my_lib"
#module_path = "../my_lib/src/my_lib/__init__.py"
#spec = importlib.util.spec_from_file_location(module_name, module_path)
#mymodule = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(mymodule)


# python -m venv venv
# source venv/bin/activate
# pip install ../my_lib/src
# or
# pip install --user /path/to/your/module

# poetry add ../my_lib
# poetry run python src/my_main_app/main.py
# poetry show my_lib
# or install global
# poetry self add ../my_lib
# or tarball or wheel
# poetry add ./mypackage-0.1.0.tar.gz
# poetry add ./mypackage-0.1.0-py3-none-any.whl


import my_lib


my_lib.my_print(my_lib.my_sum(1, 2))

print('done')
