"""Decorators
Recall the simple closure example we did which allowed us to maintain a count of ho9w many times a function was called:



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

result = add(1, 2)  # Function add was called 1 times
                    # result = 3

print(result)

I essentially modified our add function by wrapping it inside another function that added some functionally to it

I can also say that we decorated ourfunction add with the function counter

And I call counter a decorator function


In general a decorator function:
takes a function as an argument
returns a closure
the closure usually accepts any combination of parameters
runs some code in the inner function(closure)
the closure function calls the original function using the arguments passed to the closure
returns whatever is returned by that function call



        Decorators and the @ symbool

In our previous example, we saw that the counter was a decorator and we could decorate our add function using:      add = counter(add)

In general, if func is a decorator function, we decorate another function my_func using:
    my_func = func(my_func)

This is so common that Python provides a convenient way of writing that:

    @counter            (is the sameas writing)         @func
    def add(a, b):                                      def my_func(...):
        return a + b                                        ...

    is the same as writing                              is the same as writing

    def add(a, b):                                      def my_func(...):
        return a + b                                        ...

    add = counter(add)                                  my_func = func(my_func)



        Introspecting Decorated Functions

Let's use the same count decorator                         def counter(fn):
                                                            count = 0
                                                            def inner(*args, **kwargs):    # using *args. **kwargs means we can call any function fn with any combination of positional and keyword arguments
                                                                nonlocal count
                                                                count += 1
                                                                print('Function {0} was called {1} times'.format(fn.__name__, count))
                                                                return fn(*args, **kwargs)
                                                            return inner
"""
# @counter      # if not commented out, python shows it is not defined
from itertools import count


def mult(a, b, c=1):
    # returns the product of three values           I could have written:
    return a * b* c                                 # mult = counter  (the same thing as @counter)

mult.__name__      # mult is now inner              # The dunder 'name' property

help(mult)          # Help on function inner in module __main__:
                    # inner(*args, kwargs)

                    # we have lost our docstring, and even the original function signature
                    # even using the inspect module's signature does not yield better results



"""       One approach to fixing this
We can try to fix this problem, at least for the docstring and function name as follows:


def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print*'Function {0} was called {1} times'.format(fn.__name__, count)
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__        # these two have been added in to change the function
    inner.doc__ = fn.__doc__            # these two have been added in to change the function
    return inner

But this doesn't fix losing the function signature - doing so would be quite complicated



        The functools.wraps function
The functools module has a wraps function that we can use to fix the metadata of our inner function in our decorator

from functools import wraps
    in fact, the wraps function is itself a decorator
        but, it needs to know what was our 'original' function-in this case fn


"""

def counter(fn):                            # @counter
    count = 0                               # def mult(a:int, b:int, c:int=1):
    def inner(**args, **kwargs):
        nonlocal count                      # returns the product of three values
        count += 1
        print(count)                        # return a * b * c
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner


# help(mult)    Help on function mult in module __main__:
                    mult(a:int, b:int, c:int=1)
                        returns the product of three values

# and introspection using the inspect module works as expected:

# inspect.signature(multi)      # <Signature (a:int, b:int, c:int=1)

# I don't have to use wraps


                                The same thing:
                                                def counter(fn):
                                                    count = 0
                                                    @warps(fn)
                                                    def inner(**args, **kwargs):
                                                        nonlocal count
                                                        count += 1
                                                        print(count)
                                                        return fn(*args, **kwargs)
                                                    inner = wraps(fn)(inner)
                                                    return inner



