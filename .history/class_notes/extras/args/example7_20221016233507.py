# args: example6.py
import argparse
import datetime

parser = argparse.ArgumentParser(description='Returns a string contaning the name and age of the person.')
parser.add_argument('-f', '--first', help='first name', type=str, required=False)
parser.add_argument('-l', '--last', help='last name', type=str, required=True)
parser.add_argument('--yob', help='year of birth', required=False)

args = parser.parse_args()

args = parser.parse_args()

print(args)  # Namespace(first='Polly', last='Parrot', yob='1969')