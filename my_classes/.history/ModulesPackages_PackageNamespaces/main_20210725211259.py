# main.py

print('=================================')

print('Running main.py - module name: {0}'.format(__name__))

import module1

print(module1)

module1.pprint_dict('main.globals', globals())
print('=================================')  # =================================
                                            # Running main.py - module name: __main__
                                            # =================================

