# main
import shared.validators

shared.validators.is_boolean('true')
shared.validators.json.is_json('{}')
shared.validators.is_numeric()
shared.validators.is_date('2018-0101')

shared.validators.boolean.is_boolean(True)

# print('\n\n***** self *****')
# for k in dict(globals()).keys():
#     print(k)  # ***** self *****
#             # __name__
#             # __doc__
#             # __package__
#             # __loader__
#             # __spec__
#             # __annotations__
#             # __builtins__
#             # __file__
#             # __cached__
#             # common

# print('\n\n***** common *****')
# for k in common.__dict__.keys():
#     print(k)



print('\n\n***** common *****')
for k in shared,__dict__.keys():
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


print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** numeric *****
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
                    # k
