"""                         DocStrings and Default values of Named Tuples
            Default Docs for Named Tuples
When we create a named tuple class, default docstrings are created

Point2D = namedtuple('Point2D', 'x y')
    Point2D.__doc__     -> Point2D(x, y)
    Point2D.x.__doc__   -> Alias for field number 0
    Point2D.y._doc__    -> Alias for field number 1


help(Point2D)   ->      class Point2D(builtins.tuple)
                            Point2D(x, y)


                        x
                            Alias for field number 0

                        y
                            Alias for field number 1



            Overriding docstrings

We can override rhe docstrings simply by specifying values for the __doc__properties
(this is not unique to named variables!)

Point2D.__doc__ = 'Represents a 2D Cartesian coordinate.'

Point2D.x.__doc__ = 'x coordinate'

Point2D.__doc__ = 'y coordinate'


help(Point2D)   ->  class Point2D(builtins.tuple)
                        Represents a 2D Cartesian coordinate
                        x
                            x coordinate

                        y
                            y coordinate



            # Default Values
The namedtuple function does not provide us a way to define default values for each field

    Two approaches to this:

Using a Prototype
Create an instance of the named tuple with default values = the prototype
Create any additional instances of the named tuple using the prototype,_replace method
I will need to supply a default for every field (can be None)


"""