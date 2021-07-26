# modules_1.py

from pprint import pprint


print('------- Running {0} -----------'.format(__name__))
def pprint_dict(header, d):
    print('****** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('------------------------------\n\n')


pprint_dict('module1.globals', globals())

print('---------- End of {0} -------------'.format(__name__))  #------- Running __main__ -----------
                    ****** module1.globals *****
                    __name__ __main__
                    __doc__ None
                    __package__ None
                    __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x7f59f1dab0d0>
                    __spec__ None
                    __annotations__ {}
                    __builtins__ <module 'builtins' (built-in)>
                    __file__ /home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/modules_1.py
                    __cached__ None
                    pprint <function pprint at 0x7f59f1c554c0>
                    pprint_dict <function pprint_dict at 0x7f59f1c55430>
                    ------------------------------


                    ---------- End of __main__ -------------


