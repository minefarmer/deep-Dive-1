# common: main.py
import common.validators.boolean
import common.validators.date
import common.validators.json
import common.validators.numeric

validators.json.is_json('{}')
validators.date.is_date('2022-10-11')


