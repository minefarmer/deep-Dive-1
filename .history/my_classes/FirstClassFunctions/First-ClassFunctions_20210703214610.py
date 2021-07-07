"""            First-Class Functions

can be passed to a function as an argument

can be returned from a function

can be assigned to a variable

can be stored in a data structure (such as list, tuple, dictionary, etc.)



Types such as INT, FLOAT, STRING, TUPLE, LIST and many more are first-class objects.



Functions (function) are also first-class objects




            Higher-Order functions are functions that:


take a function as an argument      (e.g. the simple time we wrote in the last section)

    and/or

return a function                   (plenty of that when we cover decorators in the next section)




            Topics in this section

    function annotations and documentation

    lambda expressions and anonymous functions

    callables

    function introspection

    built-in higher order functions (such as sorted, map, filter)

    some functions in the functools module (such as reduce, all, any)

    partials




            Docstrings

We have seen the help(x) function before    -> returns some documentation (if available) for x

We can document our functions (and moduls, classes, etc) to achieve the same result using Docstrings    -> PEP 257

If the first line in the function body is a string(not an assignment, not a comment, just a string by itself), it will be interpreted as a docstring

"""

def my_func(a):                             # help(my_func)
    "documentation for my_func"
    return a                                        # -> my_func(a)
                                                    #     