"""         Decorator Parametors
In the previous ideos we saw some built-in decorators that can handle some arguments:

@wraps(fn)                  @lru_cache(maxsize=256) <\
def inner():                def factorial(n):         \
    ...                         ...                     \>function call


This should look quite differient grom the decorators we have been creating and using:

@timed  <----------- no function call
def Fibonacci(n):
    ...

"""
from symbol import parameters
from time import perf_counter
from unittest import result


def timed(fn):
    from time import perf_counter

    def inner(*arhs, **kwarrgs):
        total_elapse = 0
        for i in range(10):         # hardcoded value 10    # need to pass as a parameter
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    return inner

"""
@timed
def my_func():      or      my_func = timed(my_func)
    ...

        On e Approach to passing (line 24) as a parameter

                / <  extra parameter
def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0        /  free variable
        for i in range(reps):   <
            start = perf_counter()
            result = fn(*ars, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(avg_elapsed)
        return result
    return inner


my_func = timed(my_func, 10)



            # Rethinking the solution

@timed
def my_func():                  my_func = timed solution(my_func)
    ...

So, timed is a function that returns that inner closure that contains our original function


In order for this to work as intended:

@timed(10)
def my_func():
    ...

dec = timed(10)     # will need to return our original timed decorator when called

dec = timed(10)     # timed(10) returns a decorator
@dec
def my_func():
    ...



            # Nested closures to the rescue!
def
"""
