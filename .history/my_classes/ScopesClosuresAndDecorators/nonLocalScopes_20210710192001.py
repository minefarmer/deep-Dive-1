"""             NonLocal Scopes

        Inner Functions
We can define functions from inside another function:

"""
def outer_func():
    # some code
        # this is an example of a nested function
    def inner_func():
        # some code

    inner_func()

outer_func()
"""
Both functions have access to the global and built-in scopes as well as their respective local scopes
But the inner function also has access to its enclosing scope - the scope of the outer function
That scope is neither local (to inner_func) nor global - it is called a non local scope


        Referencing variables from the inclosing scope

Consider this example

module1.py
a = 10

def outer_func():
    print(a)

outer_func()        When we call outer_func, Python sees the reference to a



Consider this example

module1.py

def outer_func():
    print(a)

    inner_func()

outer_func()

When we call outer_func, inner_func is created and called

When inner_func is called, Python does not find a in the local(inner_func) scope

So it looks for it in the enclosing scope, in this case the scope of the outer func



Another example

module1.py
    a = 10

    def outer_func():

        def inner_func():
        print(a)

    inner_func()

outer_func()

"""

