import module1
import sys

print('=================================')
print('Running main.py - module name: {0}'.format(__name__))



print('importing module1 again...')
del globals()['module1']

import  module1

module1.pprint_dicts('main.globals', globals())




print('=================================')  #/home/rich/anaconda3/envs/Matson/bin/python /home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/main2.py
# ----------- Running module1  --------


# -----------------
# ****** module1.globals *****
# ----------------------


# ---------- End of {0} ------------ module1
# =================================
# Running main.py - module name: __main__
# importing module1 again...
# Traceback (most recent call last):
#   File "/home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/main2.py", line 14, in <module>
#     module1.pprint_dicts('main.globals', globals())
# AttributeError: module 'module1' has no attribute 'pprint_dicts'