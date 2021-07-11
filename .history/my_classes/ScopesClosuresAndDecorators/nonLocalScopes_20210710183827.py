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


