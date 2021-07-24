'''             Modifying and extending Named Tuples

            Named tuples are immutable
How we can change values inside the tuple
Just like with strings, we have to create a new tuple, with the modified values

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(0, 0)  # will not work



'''