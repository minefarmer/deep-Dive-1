# example1 - module1.py

print('------------- Running {0} ------------'.format(__name__))


def print_dict(header, d):
    print('\n\n-----------------------------------------')
    print('***** {0} *****'.format(header))
    for key, value in d():
        print(key, value)
    print('---------------------------------------------')


print_dict('module.globals', globals)

print('---------------- End of {0} --------------'.format(__name__))
