
import os.path
import types
import sys

module_name = 'module1'
module_file = 'module_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a ref in sys.modules
sys.modules[]

# compile source_code
code = compile(source_code, filename=module_abs_file)










# print('======================================')
# print('Running main.py - module name:'.format(__name__))

# import module1


# print('======================================')
# print('Running module1.py')  # ======================================
#                             # Running main.py - module name:
#                             # ======================================
#                             # Running module1.py

# def hello():
#     print('module1 says Hello!')
