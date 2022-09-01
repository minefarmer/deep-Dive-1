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
mod = ty


