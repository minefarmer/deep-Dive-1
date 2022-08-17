# timming
print('loading timing...')  # loading timing...
"""
Times how long a snippet of code takes to run
over multiple iterations.
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code,repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)


if __name__ == '__maim__':
    # print('running this command line code')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help='The Python code snippet to time.')
    parser.add_argument('-r', '--repeats', type=int, default=10, help='Number of times to repeat the test.')
    args = parser.parse_args()

    print(fargs.code)
    print(args.repeats)
