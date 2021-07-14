"""Decorators
Recall the simple closure example we did which allowed us to maintain a count of ho9w many times a function was called:

"""

def counter(fn):
    count = 0
    def imnner(*args, **kwargs):    
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    return a + b
