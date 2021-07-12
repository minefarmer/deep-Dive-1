"""                     Closuers
Free variables and closures

Remember: Functions defined inside another function can access the outer (nonLocal) variables

"""
def outer():
    x = 'python'
                                    / this x refers to the one in outer's scope', this nonlocal variable x is called a free variable
    def inner():                   /
        print("{0} rocks!".format(x))  when we consider inner, we are really      looking at:
                                            The function inner
                                            the free variable x (with the current value python)

                                            This is called a closure, # x thru the print statement

    inner()

outer()  # python rocks!

"""     Returning the inner function
What happens if, instead of calling(running) inner from inside outer, we rune it?

def outer():
    x = 'python'        # x is a free variable in inner, it is bound to the variable x in outer, this happens when outer runs

    def inner():
        print("{0} rocks!".format(x))

    return inner        # when returning inner, we are actually 'returning' the closure

We can assign that return value to a variable name:  fn = outer()

fn()  # python rocks!

When we called fn
    at that time Python determined the value of x in the extended scope
    But notice that outer had finished running before we called fn - it's scope was gone



        Python cells and Multi-Scopped Variables

def outer():        # Here the value of x is shared between two scoped
    x = 'python'        # outer
    def inner():        # inner
        print(x)
    return inner    # The label x is in two different scopes

Python does this by creating a cell as an intermediary object
outer,x ---->    # cell  0xA500     /  str   0xFF100    # indirect reference
inner.x ---->    #       OxFF199   /         python
            # they are pointing to the same cell
# when requesting the value of the variable, Python will "double-hop" to get the final value



            Closures
I can think of the closure as a function plus an EXTENDED SCOPE THAT CONTAINS THE FREE VARIABLES

The free variables's value is the object the cell points to - so that could change over time!

def outer():
    a = 100
    _______________________closure______
   |x = 'python'                        |
    def inner():
        print("{0} rocks!".format(x))  when we consider inner, we are really      looking at:
                                            The function inner
                                            the free variable x (with the current value python)

                                            This is called a closure, # x thru the print statement

    inner()

outer()  # python rocks!

"""