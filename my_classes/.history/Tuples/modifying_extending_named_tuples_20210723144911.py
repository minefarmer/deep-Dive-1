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
djia - Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393)

Suppose we only want to change the close field

'''