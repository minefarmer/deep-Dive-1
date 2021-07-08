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
l = l[5, 8, 6, 10, 9]                       # result = 5

max_value = lambda a, b: a if a > b else b  # result = max(5, 8) = 8

def max_sequence(sequence):                 # result = max(5, 6) = 8
    result = sequence[0]
    for e in sequence[1:]:                  # result = max(5, 10) = 10
        result = max_value(result, e)       # result = max(5, 10) = 10
    return result                           # result -> 10


Notice the sequence of steps:

l = [5,     8,      6,      10,]
