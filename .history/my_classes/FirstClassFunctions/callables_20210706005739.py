"""         Callables

What are callables?
Any object that can be called using the ()       # operator always return a value     -> like functions and methods    -> but it goes beyond these two...
Many other objects in Python are also callable

To see if an object is callable, we can use the builtin function: callable

callable(print) -> True
callable('abc'.upper)  ->  True
callable(str,upper)  ->  True
callable(callable)  -> True
callable(10)



        Different types of callables

built-in functions          print       len         callable

"""