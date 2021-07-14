"""Decorators
Recall the simple closure example we did which allowed us to maintain a count of ho9w many times a function was called:

"""

def counter(fn):
    count = 0
    def inner(*args, **kwargs):    # using *args. **kwargs means we can call any function fn with any combination of positional and keyword arguments
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    return a + b

add = counter(add)
