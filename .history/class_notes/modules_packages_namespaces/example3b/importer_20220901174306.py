#  3b - importer.py
import os.path
import types
import sys

def import_(module_name, module_file, module_path):
    module_rel_file_path = os.path.join.(module_path. module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read


# set a ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=moduke_abs_file_path, mode='exec')

# execute compiled source code
exec(code, mod.__dict__)

#  DONE

import module1
module1.hello()

