# args: example5.py
import argparse

parser = argparse.ArgumentParser(description='Calculates the div a//b and mod a%b of two intergers')
parser.add_argument('a', help='first integer', type=int)
parser.add_argument('b', help='second integer', type=int)

args = parser.parse_args()

a = args.a  # 10
b = args.b # 3

print(f'{a}//{b} = {a//b}, {a}%{b} = {a % b}')  # 
