# set ref in sys.modules
sys.modules[module_name] = mod

# compile source_code
code = filename=module_abs_file_path, mode='exec