# package imports: main.py
import common
import common.validators as validators
import common.modules as models
# from common.modules import *
import common.helpers as helpers


validators.is_boolean('true')
validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('2022-1013')

john_post = models.Post()
john_posts = models.Post


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