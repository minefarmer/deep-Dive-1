# package_imports: main2.py   better way
import common.validators

common.validatord.is_boolean('True')
common.validators.json.is_jason('{}')
common.validators.is_numeric(10)
common.validators.is_date('2022-1012')

common.validators.boolean.is_boolean(True)


print('\n\n***** self *****')
for k in globals().keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)