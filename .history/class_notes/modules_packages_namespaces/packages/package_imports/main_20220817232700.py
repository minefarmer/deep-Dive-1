# main.py
import common.validators.boolean
import common.validators.date
import common.validators.json
import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2018-01-01')

# print('\n\n***** self *****')
# for k in dict(globals()).keys():
#     print(k)  # ***** self *****
#             # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __annotations__
            # __builtins__
            # __file__
            # __cached__
            # common

# print('\n\n***** common *****')
# for k in common.__dict__.keys():
#     print(k)  # __name__
#                     __doc__
#                     __package__
#                     __loader__
#                     __spec__
#                     __path__
#                     __file__
#                     __cached__
#                     __builtins__
#                     validators


print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

