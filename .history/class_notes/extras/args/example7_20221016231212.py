# args: example6.py
import argparse
import datetime

parser = argparse.ArgumentParser(description='Returns a string contaning the name and age of the person.')
parser.add_argument(''-f', '--first', help='specify first name', type-str,)

