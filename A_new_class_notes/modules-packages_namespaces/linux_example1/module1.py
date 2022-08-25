# module1.py

print('---------- Running {0} -----------'.format(__name__))  # ---------- Running __main__ -----------


def pprint_dict(header, d):
    print('\n\n----------------------------------')
    print('***** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('--------------------------------------\n\n')  # ----------------------------------
        # ***** module1.globals *****
        # __name__ __main__
        # __doc__ None
        # __package__ None
        # __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x7f169dd9e340>
        # __spec__ None
        # __annotations__ {}
        # __builtins__ <module 'builtins' (built-in)>
        # __file__ /home/carl/Desktop/Matshub/deep-Dive-1/class_notes/modules_packages_namespaces/linux_example1/module1.py
        # __cached__ None
        # pprint_dict <function pprint_dict at 0x7f169dbac9d0>
        # --------------------------------------


pprint_dict('module1.globals', globals())

print('-------------------End of {0} --------------'.format(__name__))  # -------------------End of __main__ --------------

