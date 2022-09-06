# example1 - module1.py

print('------------- Running {0} ------------'.format(__name__))


def print_dict(header, d):
    print('\n\n-----------------------------------------')
    print('***** {0} *****'.format(header))
    for key, value in d.items():
        print(key, value)
    print('---------------------------------------------\n\n')


print_dict('module.globals', globals)

<<<<<<< HEAD:class_notes/modules-packages_namespaces/Modules/Example1/module1.py
print('---------------- End of {0} --------------'.format(__name__))
# TODO: 130 = 9:35
=======
print('---------------- End of {0} --------------'.format(__name__))
>>>>>>> a692f3495ab8379d2f05e9ce6f169e2129aad59a:.history/class_notes/modules-packages_namespaces/Modules/Example1/module1_20220903114528.py
