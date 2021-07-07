"""Function Introspection
            Functions are first class objects

They have attributes        __doc__     __annotations__

We can attach our own attributes

"""
def my_func(a, b):
    return a + b

my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category)  # math

print(my_func.sub_category)  # arithmetic