# main
import common.validators

common.validators.boolean.is_boolean('true')
# import common.validators.date
# import common.validators.json
# import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2018-01-01')

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


# print('\n\n***** validators *****')
# for k in common.__dict__.keys():
#     print(k)  # ***** common *****
#             # __name__
#             # __doc__
#             # __package__
#             # __loader__
#             # __spec__
#             # __path__
#             # __file__
#             # __cached__
#             # __builtins__
#             # validators


# print('\n\n***** numeric *****')
# for k in common.validators.numeric.__dict__.keys():
    # print(k)  # ***** validators *****
#             # __name__
#             # __doc__
#             # __package__
#             # __loader__
#             # __spec__
#             # __path__
#             # __file__
#             # __cached__
#             # __builtins__
#             # boolean
#             # date
#             # json
#             # numeric


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


