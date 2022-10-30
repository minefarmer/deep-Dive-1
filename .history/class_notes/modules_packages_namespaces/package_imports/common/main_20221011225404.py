# common: main.py
import validators.boolean
import validators.date
import validators.json
import common.validators.numeric

common.validators.json.is_json('{}')
common.validators.date.is_date('2022-10-11')


