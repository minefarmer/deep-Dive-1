# args: example5.py
import argparse

parser = argparse.ArgumentParser(description='Calculates the div a//b and mod a%b of two intergers')
parser.add_argument('a', help='first integer', type=int)
parser.add_argument('b', help='second integer', type=int)

args = parser.parse_args(['100', '300'])

print(args.a)  # 100
print(args.b)  # 300

