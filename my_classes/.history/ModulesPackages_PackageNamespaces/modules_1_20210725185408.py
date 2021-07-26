# modules_1.py

from pprint import pprint

print('------- Running {0} -----------'.format(__name__))
def print_dict(header, d):
    print('****** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('------------------------------\n\n')

pprint_dict('module1.globals', globals())

print('---------- End of ')


