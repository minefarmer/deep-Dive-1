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
"""[summary]
"""
Both functions have access to the global and built-in scopes as well as thier respective local scopes

