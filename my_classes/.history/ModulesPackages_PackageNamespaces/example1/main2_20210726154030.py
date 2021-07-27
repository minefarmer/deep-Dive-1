import module1
import sys

print('=================================')
print('Running main.py - module name: {0}'.format(__name__))



print('importing module1 again...')
del globals()['module1']

import  module1

module1.pprint_dicts('main.globals', globals())




print('=================================')  #