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
l2 = [10, 20, 30]

def add(x, y):
    return x + y

list(map(add, l1, l2))      # [11, 22, 33]


"""The filter function

filter(func, iterable)

    iterable        -> a single iterable

    func            -> some function that takes a single argument


filter(func, iterable) will then return an iterator that contains all the elements of the iterable for which the function called on it is Truthy

If the function is None, it simply returns the elements of iterable that are Truthy


Examples
"""

l = [0, 1, 2, 3, 4]     # 0 is Falsey, all the other numbers are Truthy

list(filter(None, l))       # [1, 2, 3, 4]


def is_even(n):
    return n % 2 == 0


list(filter(is_even, l))    # [0, 2, 4]

list(filter(lambda n: n % 2 == 0, l))   # [0, 2, 4]




"""The zip function         zip(*iterables)     # this is not a high order function that takes multiple iterables and return one interable

[1, 2, 3, 4]        zip
                #-------->  (1, 10), (2, 20), (3, 30), (4, 40)
(10, 20, 30, 40)


[1, 2, 3]           zip
[10, 20, 30]      #-------->    (1, 10, 'a'), (2, 20, 'b'), (3, 30. 'c')
['a', 'b', 'c']


[1, 2, 3, 4, 5]
                    #-------->   (1, 10), (2, 20), (3, 30)
[10, 20, 30]

"""
