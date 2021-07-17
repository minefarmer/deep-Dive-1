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
from unittest import result


def timed(fn):
    from time import perf_counter

    def inner(*arhs, **kwarrgs):
        total_elapse = 0
        for i in range(10):         # hardcoded value 10
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    return inner


@timed
def my_func():      or      my_func 


"""


"""