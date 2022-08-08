# set ref in sys.modules
sys.modules[module_name] = mod

# compile source_code
code = compile(sourcefilename=module_abs_file_path, mode='exec