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


def my_func(a, b=2, c=3, *, kw1, kw2-2):
    pass

my_func.__name__        # my_func

my_func.__defaults__    # (2, 3)

my_func.__kwdefaults__  # {'kw2',: 2}


