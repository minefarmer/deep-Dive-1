import module1
import sys

print('=================================')

print('Running main.py - module name: {0}'.format(__name__))

print(module1)

module1.pprint_dict('main.globals', globals())



print('=================================') 