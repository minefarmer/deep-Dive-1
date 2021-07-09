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
        getitem(s, 1)  # 2

itemgetter(i)  # returns a callable which takesone parameter: a sequence object

            f = itemgetter(1)
            s = [1, 2, 3]           s = 'python'
            f(s)    # 2             f(s)    # 'y'

I can pass more than one index to tem getter:

l = [1, 2, 3, 4, 5, 6]
s = 'python'
f = itemgetter(1, 3, 4)
f(l)    # (2, 4, 5)
f(s)    # ('y', 'h', 'o')



            Attribute Getters

The attrgetter function is similarto itemgetter, but is used to retrive object attributes

It also returns a callable, that takes thr object as an argument

Suppose my_obj
"""
