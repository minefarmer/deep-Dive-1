# main.py
import common.validators.boolean
import common.validators.date
import common.validators.json
import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2018-01-01')

# print('\n\n***** self *****')
# for k in dict(globals()).keys():
#     print(k)  

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)  


# print('\n\n***** validators *****')
# for k in common.validators.__dict__.keys():
#     print(k)  


# print('\n\n***** validators *****')
# for k in common.validators.numeric.__dict__.keys():
#     print(k)  # ***** validators *****
#             # __name__
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

