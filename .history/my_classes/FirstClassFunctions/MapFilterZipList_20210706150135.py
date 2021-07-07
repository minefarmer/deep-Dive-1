"""Map Filter Zip List Comprehensions
            Higher order functions

A function that takes a function as a parameter and/or returns a function as it's return value

Example: sorted

        map   _
               |
               --  modern alternative -> list comprehensions and generator expressions
               |
        filter -



        The map function

map(func, *iterables)

    *iterables      -> avariable number of iterable objects

    func            -> some function that takes a many arguments as there are iterable objects passed to iterables

map(func, *iterables) will then return an iterator that calculates the function applied to each element of the iterables

    The iterator stops as soon as one of the iterables has been exhausted, so, unequal length iterables can be used

        Examples
"""
l = [2, 3, 4]

def sq(x):
    return x**2

list(map(sq, l))        # [4, 9, 19]


l1 = [1, 2, 3]
