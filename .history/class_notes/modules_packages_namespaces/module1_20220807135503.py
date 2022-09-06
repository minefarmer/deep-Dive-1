# Module1

print('------------- Running {0}  ----------'.format(__name__))

def pprint_dict(header, d):
    print('\n\n------------------------------')
    print('****** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('------------------------------\n\n')

pprint_dict('module.globals', globals())

print('------------- End of {0} ----------'.format(__name__))  # ------------- Running __main__  ----------


                                                                ------------------------------
                                                                ****** module.globals *****
                                                                __name__ __main__
                                                                __doc__ None
                                                                __package__ None
                                                                __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x00000264B948A100>
                                                                __spec__ None
                                                                __annotations__ {}
                                                                __builtins__ <module 'builtins' (built-in)>
                                                                __file__ c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\module1.py
                                                                __cached__ None
                                                                pprint_dict <function pprint_dict at 0x00000264B99DFEE0>
                                                                ------------------------------


                                                                ------------- End of __main__ ----------
