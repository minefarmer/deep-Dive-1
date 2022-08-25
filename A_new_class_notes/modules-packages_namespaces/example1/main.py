import sys
# main.py

# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# print('===================================')  # ===================================
                                            # Running main .py - module name: __main__
                                            # ===================================


# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# import module1



# print('===================================')  # ===================================
                                            # Running main .py - module name: __main__
                                            # ---------------- Running module1 -----------------


                                            # --------------------------------
                                            # ****** {0}| ***** module.globals
                                            # __name__ module1
                                            # __doc__ None
                                            # __package__ 
                                            # __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x0000021199F5B4F0>
                                            # __spec__ ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x0000021199F5B4F0>, origin='c:\\Users\\pgold\\MatsHub\\deep-Dive-1\\class_notes\\modules_packages_namespaces\\Example1\\module1.py')
                                            # __file__ c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\Example1\module1.py
                                            # __cached__ c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\Example1\__pycache__\module1.cpython-39.pyc
                                            # __builtins__ {'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 'copyright': Copyright (c) 2001-2022 Python Software Foundation.
                                            # All Rights Reserved.

                                            # Copyright (c) 2000 BeOpen.com.
                                            # All Rights Reserved.

                                            # Copyright (c) 1995-2001 Corporation for National Research Initiatives.
                                            # All Rights Reserved.

                                            # Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
                                            # All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
                                            #     for supporting Python development.  See www.python.org for more information., 'license': See https://www.python.org/psf/license/, 'help': Type help() for interactive help, or help(object) for help about object.}  
                                            # pprint_dict <function pprint_dict at 0x000002119A2FA0D0>
                                            # --------------------------------


                                            # --------------------------- End of (0) -----------------
                                            # ===================================



# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# import module1

# print(module1)

# module1.pprint_dict('main.globals', globals())

# print('===================================')  # ****** {0}| ***** main.globals

                                            # __name__ __main__
                                            # __doc__ None
                                            # __package__ None
                                            # __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x0000025A5A8DA100>
                                            # __spec__ None
                                            # __annotations__ {}
                                            # __builtins__ <module 'builtins' (built-in)>
                                            # __file__ c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\Example1\main.py
                                            # __cached__ None
                                            # module1 <module 'module1' from 'c:\\Users\\pgold\\MatsHub\\deep-Dive-1\\class_notes\\modules_packages_namespaces\\Example1\\module1.py'>
                                            # --------------------------------


                                            # ===================================



# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# import module1

# print(module1)

# module1.pprint_dict('main.globals', globals())

# print(sys.path)  # ['c:\\Users\\pgold\\MatsHub\\deep-Dive-1\\class_notes\\modules_packages_namespaces\\Example1', 'C:\\Users\\pgold\\anaconda3\\python39.zip', 'C:\\Users\\pgold\\anaconda3\\DLLs', 'C:\\Users\\pgold\\anaconda3\\lib', 'C:\\Users\\pgold\\anaconda3', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\Pythonwin']

# print('===================================')  # ****** {0}| ***** main.globals



# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# import module1

# print(module1)

# module1.pprint_dict('main.globals', globals())

# print(sys.path)

# print(sys.modules['module1'])

# print('===================================')  # ****** {0}| ***** main.globals  # ['c:\\Users\\pgold\\MatsHub\\deep-Dive-1\\class_notes\\modules_packages_namespaces\\Example1', 'C:\\Users\\pgold\\anaconda3\\python39.zip', 'C:\\Users\\pgold\\anaconda3\\DLLs', 'C:\\Users\\pgold\\anaconda3\\lib', 'C:\\Users\\pgold\\anaconda3', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\pgold\\anaconda3\\lib\\site-packages\\Pythonwin']


# print('===================================')

# print('Running main .py - module name: {0}'.format(__name__))

# import module1

# print('Importing module1 again...')
# del globals()['module1']

# module1.pprint('main.globals', globals())

# print('===================================')  # Importing module1 again...
                                            # Traceback (most recent call last):
                                            #   File "c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\Example1\main.py", line 127, in <module>
                                            #     module1.pprint('main.globals', globals())
                                            # NameError: name 'module1' is not defined



print('===================================')

print('Running main .py - module name: {0}'.format(__name__))

import module1

print('Importing module1 again...')
del globals()['module1']

import module1

module1.pprint_dict('main.globals', globals()) 

print('===================================')  # Importing module1 again...
                                                # --------------------------------
                                                # ****** {0}| ***** main.globals
                                                # __name__ __main__
                                                # __doc__ None
                                                # __package__ None
                                                # __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x00000248F121A100>
                                                # __spec__ None
                                                # __annotations__ {}
                                                # __builtins__ <module 'builtins' (built-in)>
                                                # __file__ c:\Users\pgold\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\Example1\main.py
                                                # __cached__ None
                                                # sys <module 'sys' (built-in)>
                                                # module1 <module 'module1' from 'c:\\Users\\pgold\\MatsHub\\deep-Dive-1\\class_notes\\modules_packages_namespaces\\Example1\\module1.py'>
                                                # --------------------------------


print('Running main .py - module name: {0}'.format(__name__))

import module1

print('Importing module1 again...')
del globals()['module1']

import module1

module1.pprint_dict('main.globals', globals())
