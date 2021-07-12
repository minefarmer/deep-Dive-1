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
                                        |
    def inner():
        a = 10  # local variable        |
        print("{0} rocks!".format(x))   |
    |___________________________________|
    return inner
fn = outer()        fn -> inner   + extended scope  x



            Introspection

def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10  # local variable
        print("{0} rocks!".format(x))
    return inner
fn = outer()

fn.__code__.co_freevars     ->('x',)    (a is not a free variable)

fn.__closure__              -> (<cell at )xA500: str object at 0xFF199>,


def outer():
    x = 'python'
    print(hex(id(x)))   -----------------> 0xFF100      indirect reference
    def inner():
        print(hex(id(x)))   -----------------> 0xFF100      indirect reference
        print("{0} rocks!".format(x))
    return inner

fn = outer()
fn()


def counter():  # closure
------------------------
    count = 0         / count is a free variable
                     /  it is bound to the cell count
    def inc():      /
        nonlocal count
        count += 1
        return count
------------------------
    return inc
                fn -> inc + count -> 0
                /
fn = counter() /

fn()    => 1    count's (indirect) reference changed from object 0 to the object 1

fn()    => 2

Every  time we run a function a new scope is created.

If that function generates a closure, a new closure is created every time as well

def counter():  # closure       f1 = counter()
------------------------        f2 = counter()
    count = 0
                                f1()    # 1
    def onc():                  f1()    # 2         f1 and f2 do not have the same extended scope
        nonlocal count          f1()    # 3
        count += 1
        return count            f2()    # 1         they are different instances of the closure
-------------------------
    return inc                                      the cells are different



def outer():

    count = 0
                    count is a free variable-bound to count in the extended scope
    def inc1():     /
        nonlocal count
        count = 1
        return count
                    count is a free variable - bound to the same count
    def inc2():     /
        nonlocal count
        count += 1
        return count
                    /   returns a tuple containing both closures
    return inc1, inc2

f1, f2 = outer()

f1() -> 1
f2() -> 2


The shared extended scope is not unusual

def adder(n):
    def inner(x):
        return x + n

return inner

"""