#  3b - importer.py
import os.path
import types
import sys

def



# set a ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=moduke_abs_file_path, mode='exec')

# execute compiled source code
exec(code, mod.__dict__)

#  DONE

import module1
module1.hello()

