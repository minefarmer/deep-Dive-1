# main.py
import os.path
import types
import sys

module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)  # this is a relative path.
module_abs_file_path = os.path.abspath(module_rel_file_path)  # this is an absolute path.

# read the source code from file.
with open(module_rel_file_path, 'r') as code_file:
    source = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exe4c')

# execute compiled source code
exec(code, mod.__dict__)

# Done

mod.hello()  # 
            Traceback (most recent call last):
            # File "c:\Users\Rich Matson\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\example_3a\main.py", line 14, in <module>
            #     with open(module_rel_file_path, 'r') as code_file:
            # FileNotFoundError: [Errno 2] No such file or directory: '.\\module1_source.py'
