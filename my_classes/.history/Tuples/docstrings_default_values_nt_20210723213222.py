"""                         DocStrings and Default values of Named Tuples
            Default Docs for Named Tuples
When we create a named tuple class, default docstrings are created

Point2D = namedtuple('Point2D', 'x y')
    Point2D.__doc__     -> Point2D(x, y)
    Point2D.x.__doc__   -> Alias for field number 0
    

"""