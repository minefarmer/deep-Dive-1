"""The operator module
        Functional Equivalents to operators

In the last lecture we wrote code such as:

l = [2, 3, 4]

reduce(lambda a, b: a * b, l)

We used a lambda expression to create a functional version of the * operator

This is something that happens quite often, so the operator module was created

This module is a convenience module

I can always use my own functions and lambda expressions instead




            The operator module

Arithmetic Functions
"""
add(a, b)
mul(a, b)
pow(a, b)
mod(a, b)
floordiv(a, b)
neg(a)
        # and many more

lt(a, b)    # less than
le(a, b)    # less than or equal

gt(a, b)    # greater than
ge(a, b)    # greater than or equal to

eq(a, b)    # equal to
ne(a, b)    # not equal to

is_(a, b)   # is
is_not(a,b) # is not

and_(a, )   # and
or_(a, b)   # or
not_(a, b)   # not


"""         Sequence/mapping operators

concat(s1, s2)

contains(s, val)

countOf(s, val)

getitems(s, i)  ------------------------
                                        \
setitem(s, i, val)                       \
                    | mutable objects  ---| variants that use slices
delitem(s, i)  --------------------------/


            Item getters

The item getter function returns a callable

getitems(s, i)      takes two parameters, and returns a value: s[i]

        s = [1, 2, 3]
        getitem(s, 1)

"""
