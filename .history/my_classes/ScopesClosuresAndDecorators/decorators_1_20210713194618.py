"""Decorators
Recall the simple closure example we did which allowed us to maintain a count of ho9w many times a function was called:

"""

def counter(in):
    count = 0
    def imnner(*args, **kwargs):
        nonlocal count += 1
        print('Function ')