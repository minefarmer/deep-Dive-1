# args: example1
import sys

print(sys.argv)


sh-5.1$ python3 example1.py 10 20 30
['example1.py', '10', '20', '30']
sh-5.1$ python3 example1.py 10 20 30 John Cleese Eric Idle
['example1.py', '10', '20', '30', 'John', 'Cleese', 'Eric', 'Idle']