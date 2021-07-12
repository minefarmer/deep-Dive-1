"""                     Closuers
Free variables and closures

Remember: Functions defined inside another function can access the outer (nonLocal) variables

"""
def outer():
    x = 'python'

    def inner():
        print("{0} rocks!".format(x))

    def inner()

