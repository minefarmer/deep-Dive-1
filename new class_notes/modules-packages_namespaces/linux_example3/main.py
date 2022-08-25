# main.py
import sys
import importer

module1 = importer.import_('module1','module1_source.py', '.')  # Prints  Running importer.py, Running module1.py

print('sys says:', sys.modules.get('module1 not found'))

import module2
module2.hello()  # Running importer.py
                # Running module1.py
                # sys says: None
                # Running module2.py
                # module2 says Hello!
                # and...
                # module1 says Hello!


'''

>>> sys.path
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/home/carl/.local/lib/python3.9/site-packages', '/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.9/dist-packages']
>>> 

'''
