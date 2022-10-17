# args: example5.py
import sys

keys = sys.argv[1::2]
values = sys.argv[2::2]

print(keys)  # []
print(values)  # []


# print(list(zip(keys, values)))  # ['--last-name', '--first-name']
                                  # ['Cleese', 'John']
                                  # {'--last-name': 'Cleese', '--first-name': 'John'}

args = {k: v for k, v in zip(keys, values)}

print(args)

first_name = args.get('--first-name', None)
last_name = args.get('--last-name', None)

print(first_name)
