# module1.py

print('-----------Running {0} -------------', format(__name__))  # -----------Running {0} ------------- __main__


def print_dict(header, d):
    print('\n\n----------------------------------------------------')
    print('***** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('\n\n-------------------------------------------')

print_dict('module1.globals', globals())

print('----------- End of {0} -------------'.format(__name__))  # -----------Running {0} ------------- __main__
# 
# 
# ----------------------------------------------------
# ***** module1.globals *****
# __name__ __main__
# __doc__ None
# __package__ None
# __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x000002B26597A100>
# __spec__ None
# __annotations__ {}
# __builtins__ <module 'builtins' (built-in)>
# __file__ c:\Users\Rich Matson\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\example_1\module1.py
# __cached__ None
# print_dict <function print_dict at 0x000002B265EA98B0>


# -------------------------------------------
# ----------- End of __main__ -------------
# -----------Running {0} ------------- __main__


# ----------------------------------------------------
# ***** module1.globals *****
# __name__ __main__
# __doc__ None
# __package__ None
# __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x000002B26597A100>
# __spec__ None
# __annotations__ {}
# __builtins__ <module 'builtins' (built-in)>
# __file__ c:\Users\Rich Matson\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\example_1\module1.py
# __cached__ None
# print_dict <function print_dict at 0x000002B265EA98B0>


# -------------------------------------------
# ----------- End of __main__ -------------
