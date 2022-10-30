# package_imports: main.py
import common.validators.boolean
import common,validators.date
import common.validators.jason
import common.validators.numeric


common.validators.json.is_json('{}')
common.validators.date.is_date('2022-10-01')

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

