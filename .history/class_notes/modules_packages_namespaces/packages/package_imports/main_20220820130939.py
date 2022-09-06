#  package imports main
import common.validators.boolean
import common.validators.date
import common.validators.json
import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2018-01-01')

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
__name__
__doc__
__package__
__loader__
__spec__
__annotations__
__builtins__
__file__
__cached__
common

