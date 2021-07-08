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
from msilib import sequence
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


_reduce(lambda a, b: a if a > b else b, l)  # maximum

_reduce(lambda a, b: a if a < b else b, l)  # minimum




#       Adding all the elements to a list

add = lambda a, b: a+b
                                    # result = 5
l  = [5, 8, 6, 10, 9]
                                    # result = add(5, 8) = 13

                                    # result = add(13, 6) = 19

def _reduce(fn, sequence):          # result = add(19, 10) = 29
    result = sequence[0]
    for x in sequence[1:]:          # result = add(29. 9) = 38
        result = fn(result, x)
    return result                   #       result = 38

_reduce(add. l)




"""     The functools module

Pthon implements a reduce function that will handle any iterable, but works similarly to what I just saw.

"""

from functools import reduce

l = [5, 8, 6, 10, 9]

reduce(lambda a, b: a if a > b else b, l)   # max -> 10

reduce(lambda a, b: a if a < b else b, l)   # min -> 5

reduce(lambda a, b: a if a + b, l)          # sum -> 38


#   reduce works on any iterable

reduce(lambda a, b: a if a < b else b, {10, 5, 2, 4})   # 2

reduce(lambda a, b: a if a < b else b, 'python')    # h

reduce(lambda a, b: a + ' ' + b else b, ('python', 'is', 'awesome'))   # 'python is awesome'

"""         Built-in Reducing Functions
Python provides several common reducing functions:

min     min([5, 8, 6, 10, 9])   # 5

max     max([5, 8, 6, 10, 9])   # 10

sum     sum([5, 8, 6, 10, 9])   # 38

any     any(l)  # True if any element in l is truthy
                # False otherwise

all     all(l)  # True if every element in l is truthy
                # False otherwise


            Using reduce to reproduce any

l = [0, '', None, 100]

result = bool(0) or bool('') or bool(None) or Bool{100}

            Note: 0 or '' or None or 100 -> 100     bu we want our result to be True/False so we use bool()

Here we just need to repeatedly apply  the or  operator to the truth values of each element.

result = bool(0)                # False

result = result or bool ('')    # False

result = result or bool(None)   # False

result = result or bool(100)    # True


reduce(lambda a, b: bool(a), l) # True


            Calculating the product of all elements in an iterable

No built-in method to do this

But, very similar to how we added all the elements in an iterable or sequence:

[1, 3, 5, 6]    # 1 * 3 * 5 * 6

reduce(lambda a, b: a * b, l)

res = 1

res = res * 3 = 3

res = res * 5 = 3 * 5 = 15

res = res * 6 = 15 * 6 = 90     = 1 * 3 * 5 * 6


            # Special case: Calculating n!

n! = 1 * 2 * 3 * ... * n            # 5! = 1 * 2 * 3 * 4 * 5

range(1, 6)

To caculate n! we need to find the product of all the elements in range(1, n+1)

reduce(lambda a, Bb: a * b, range(1, 5+1)   # 5!



            # THE REDUCE INITIALIZER

The reduce function has a third (optional) parameter: initializer       (defaults to None)

If it is specified, it is essentially like adding it to the front of the iterable.

l = []
reduce(lambda x, y: x+y, l, 1)  # exception

l = []
reduce(lambda x, y: x+y, l, 1)  # 1

l = [1, 2, 3]
reduce(lambda x, y: x+y, l, 1)  # 7

l = [1, 2, 3]
reduce(lambda x, y: x+y, l, 100)  # 106

"""
