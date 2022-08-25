# main
import common.validators

common.validators.boolean.is_boolean('true')


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
__name__
__doc__
__package__
__loader__
__spec__
__path__
__file__
__cached__
__builtins__
validators
