# args: example5.py
import argparse

parser = argparse.ArgumentParser(description='Calculates the div a//b and mod a%b of two intergers')
parser.add_argument('a', help='first integer', type=int)
parser.add_argument('b', help='second integer', type=int)

args = parser.parse_args()

a = args.a  # 10
b = args.b # 3

print(f'{a}//{b} = {a//b}, {a}%{b} = {a % b}')  # 10//3 = 3, 10%3 = 1


sh-5.1$ /bin/python /home/rich/Desktop/Mathub/deep-Dive-1/class_notes/extras/args/example6.py -h
usage: example6.py [-h] a b

Calculates the div a//b and mod a%b of two intergers

positional arguments:
  a           first integer
  b           second integer

options:

