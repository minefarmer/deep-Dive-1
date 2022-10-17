# args: example2
import sys

numbers = sys.argv[1:]

print(sum(numbers))  # sh-5.1$ python3 example2.py 10 20 30
# Traceback (most recent call last):
#   File "/home/rich/Desktop/Mathub/deep-Dive-1/class_notes/extras/args/example2.py", line 6, in <module>
#     print(sum(numbers))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


