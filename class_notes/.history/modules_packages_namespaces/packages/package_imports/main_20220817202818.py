# main
import shared.validators

shared.validators.is_boolean('true')
shared.validators.json.is_json('{}')
shared.validators.is_numeric()
shared.validators.is_date('2018-0101')

shared.validators.boolean.is_boolean(True)

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in shared,__dict__.keys():
    print(k)


print('\n\n***** validators *****')
for k in shared.validators.__dict__.keys():
    print(k)


print('\n\n***** numeric *****')
for k in shared.validators




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
