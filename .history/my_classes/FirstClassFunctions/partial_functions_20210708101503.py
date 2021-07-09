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