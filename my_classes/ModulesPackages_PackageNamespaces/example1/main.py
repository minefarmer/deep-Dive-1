import module1
import sys

print('=================================')

print('Running main.py - module name: {0}'.format(__name__))

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)

print(sys.modules['module1'])

print('=================================')  # /home/rich/anaconda3/envs/Matson/bin/python /home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/main.py
----------- Running module1  --------


-----------------
****** module1.globals *****
----------------------


---------- End of {0} ------------ module1
=================================
Running main.py - module name: __main__
<module 'module1' from '/home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/module1.py'>


-----------------
****** main.globals *****
----------------------


['/home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1', '/home/rich/anaconda3/envs/Matson/lib/python38.zip', '/home/rich/anaconda3/envs/Matson/lib/python3.8', '/home/rich/anaconda3/envs/Matson/lib/python3.8/lib-dynload', '/home/rich/anaconda3/envs/Matson/lib/python3.8/site-packages']
<module 'module1' from '/home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/module1.py'>
=================================

