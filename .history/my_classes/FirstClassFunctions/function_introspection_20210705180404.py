"""Function Introspection
            Functions are first class objects

They have attributes        __doc__     __annotations__

We can attach our own attributes


def my_func(a, b):
    return a + b

my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category)  # math

print(my_func.sub_category)  # arithmetic


print(dir(my_func))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'category', 'sub_category']



        Function Attributes:__name__, __defaults__, __kwdefaults__

__name__        -> name of function

__defaults__    -> tuple containing positional parameter defaults

__kwdefaults__  -> dictionary containing keyword-only parameter defaults

"""


def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass

my_func.__name__        # my_func

my_func.__defaults__    # (2, 3)

my_func.__kwdefaults__  # {'kw2',: 2}



#       Function Attribute:__code__

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b                          # my_func.__code__
                                            # <code object my_func at 0x00020EEF ..

"""
This __code__ object itself has various properties, which include:

co_varnames     # parameter and local variables
                my_func.__code__.co_varnames    -> ('a', 'b', 'args', 'i')
                parameter names first, followed by local variable names

co_argcount     number of parameters
                my_func,__code__.co
"""
