# 3b main.py
import sys
import importer

module1 = importer.import_('module1', 'module1_source.py', '.')

print()

# # set a ref in sys.modules
# sys.modules[module_name] = mod

# # compile source_code
# code = compile(source_code, filename=module_abs_file_path, mode='exec')

# # execute compiled source code
# # exec(code, mod.__dict__)

# #  DONE

# # mod.hello()  # Running module1.py...  ## not working in visual studio code
#             # module1 says Hello!
TODO