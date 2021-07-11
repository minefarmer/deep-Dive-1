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
"""

