"""Reducing Functions in Python
These are functions that recombine an iterable recursively, ending up with a single return value

Also called accumulators, aggregators, or folding functions



        Example: Finding the maximum value in an iterable

a0, a1, a2, ...,, aN-1
max(a, b) _> maximum of a and b

result =a0
result = max(result, a1)
result = max(result, a2)
...
result = max(result, an-1)
    # max value in a0, a1, a2, ..., an-1

the special case of sequences
(i.e. we can use indexes to access elements in the sequence)

        Using a loop
"""
from unittest import result


l = l[5, 8, 6, 10, 9]                       # result = 5

max_value = lambda a, b: a if a > b else b  # result = max(5, 8) = 8

def max_sequence(sequence):                 # result = max(5, 6) = 8
    result = sequence[0]
    for e in sequence[1:]:                  # result = max(5, 10) = 10
        result = max_value(result, e)       # result = max(5, 10) = 10
    return result                           # result -> 10


Notice the sequence of steps:
l = l[5, 8, 6, 10, 9]                       # result = 5

max_value = lambda a, b: a if a > b else b  # result = max(5, 8) = 8

def max_sequence(sequence):                 # result = max(5, 6) = 8
    result = sequence[0]
    for e in sequence[1:]:                  # result = max(5, 10) = 10
        result = max_value(result, e)       # result = max(5, 10) = 10
    return result                           # result -> 10

l = [5,     8,  6,      10,     9]
     ^      |   |       |       |
     |      |   |
     5      |   |
      \     |   |
    max(5,  8)  |       |       |
        8       |
        \       |
         \      |
      max(8,    6)
          8             |       |
          \
        max(8,          10)
            10
             \                  |
        max(10,                 9)
                10

            result -> 10




To caculate the min:        # I just need to  change (max) to (min)
l = l[5, 8, 6, 10, 9]                       # result = 5

min_value = lambda a, b: a if a > b else b  # result = max(5, 8) = 8

def min_sequence(sequence):                 # result = max(5, 6) = 8
    result = sequence[0]
    for e in sequence[1:]:                  # result = max(5, 10) = 10
        result = min_value(result, e)       # result = max(5, 10) = 10
    return result                           # result -> 10



# I could just write:

def _reduce(fn, sequence):
    result = sequence[0
    for x in sequence[1:]]:
        result = fn(result, x)
    return result


_reduce
