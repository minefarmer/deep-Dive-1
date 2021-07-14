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

    @counter                (is the same@func
    def add(a, b):
        return a + b

    is the same as writing

    def add(a, b):
        return a + b

    add = counter(add)

"""