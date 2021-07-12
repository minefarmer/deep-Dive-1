"""                     Closuers
Free variables and closures

Remember: Functions defined inside another function can access the outer (nonLocal) variables

"""
def outer():
    x = 'python'
                                    / tis x refers to the one in outer
    def inner():                   /
        print("{0} rocks!".format(x))

    inner()

