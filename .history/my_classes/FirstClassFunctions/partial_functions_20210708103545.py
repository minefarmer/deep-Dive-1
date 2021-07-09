"""Reducing Function Arguments

"""
def my_func(a, b, c):
    print(a, b, c)

def fn(b, c):
    return my_func(10, b, c)        # fn(20, 30)  -> 10, 20, 30

f =lambda b, c: my_func(10, b, c)

from functools import partial

f = partial(my_func, 10)

f(20, 30)   # 10, 20, 30



#           Handling more complex arguments

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)


f = partial(my_func, 10, k1='a')


def pow(base, exponent):
    return base ** exponent


square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

square(5)   # 25

cube(5)     # 125

cube
