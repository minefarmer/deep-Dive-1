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

    return inner        # when returning

"""

