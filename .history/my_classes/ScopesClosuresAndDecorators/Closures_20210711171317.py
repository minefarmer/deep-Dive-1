"""                     Closuers
Free variables and closures

Remember: Functions defined inside another function can access the outer (nonLocal) variables

"""
def outer():
    x = 'python'
                                    / tis x refers to the one in outer's scope', this nonlocal variable x is called a free variable
    def inner():                   /
        print("{0} rocks!".format(x))  when we consider inner, we are really      looking at:
                                            The function inner
                                            the free variable x (with the current value python)

                                            This is called a closure, # x thru the print statement

    inner()

outer()  # python rocks!

        """[summary]
        """

