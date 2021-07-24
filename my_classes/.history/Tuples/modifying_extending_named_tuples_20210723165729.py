'''             Modifying and extending Named Tuples

            Named tuples are immutable
How we can change values inside the tuple
Just like with strings, we have to create a new tuple, with the modified values

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(0, 0)  # will not work

Suppose we need to change the value of the x coordinate:
    Simple approach:  pt = Point2P(100, pt.y)
        Note: the memory address of pt has now changed
            This approach can work well, but it has a major drawback

Stock = namedtuple('Stock", 'symbol year month day open high low close')
djia = Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393)


        the _replace instance method

The replace instance method

Named tuples have a very handy instance method, _replace

It will copy the named tuple into a new one, replacing any values from keyword arguments

The keword arguments are simply the field names in the tuple and the new value

The keyword name must match an existing field name




        the _replace instance method

from collections import namedtuple


Stock = namedtuple('Stock", 'symbol year month day open high low close')
djia = Stock('DJIA', 2021, 7, 22, 26313, 26458, 26260, 26393)

djia = djia._replace(day=23, high=26459, close=26_394)

djia = Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26394)



        Extending a named tuple

Sometimes we want to create a named tuple that extends another named tuple, appending one or more fields

Stock = namedtuple('Stock", 'symbol year month day open high low close')

We want to create a new named tuple class, StockExt that adds a single field, previous_close
When dealing with classes, this is sometimes done by using subclassing.
But this is not easy to do with named tuples
    and there is a cleaner way of doing it anyway

Point2D = namedtuple('Point2D', 'x y')

We want create a Point3D named tuple that has an extra parameter

'''


