# common main
import common.validators. boolean
import common.validators.date
import common.validators.json
import commom.validators.numeric

common.balidators.json.is_json
import common.validators.date.('2022-01-01')


common.validators.booleanis_boolean('true')


print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** numeric *****
#                     # __name__
#                     # __doc__
#                     # __package__
#                     # __loader__
#                     # __spec__
#                     # __annotations__
#                     # __builtins__
#                     # __file__
#                     # __cached__
#                     # common
#                     # k

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
