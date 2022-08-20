#  package imports main
import shared.validators

shared.validators.boolean.is_boolean('true')
shared.validators.json.is_json('{}')
shared.validators.is_numeric(10)
shared.validators.is_date('2018-0101')

common.validators.is_boolean(True)
# print('\n\n***** self *****')
# for k in globals().keys():
#     print(k)  # ***** self *****
            # __name__
            # Traceback (most recent call last):
            # File "c:\Users\Rich Matson\MatsHub\deep-Dive-1\class_notes\modules_packages_namespaces\packages\package_imports\main.py", line 11, in <module>
            #     for k in globals().keys():
            # RuntimeError: dictionary changed size during iteration



print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** self *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __annotations__
            # __builtins__
            # __file__
            # __cached__
            # common


print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)  # ***** common *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # validators


print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)  # ***** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric


print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)  # ***** numeric *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __file__
            # __cached__
            # __builtins__
            # is_integer
            # is_numeric
            # numeric_helper_1
            # numeric_helper_2





