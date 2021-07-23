"""             Tuple as Data Structure
We have see how we interpreted tuples as data structures

The position of the object contained in the tuple gives it meaning

For example, we can represent a 2D coordinate as: (10, 20)
                                                    x   y

If pt is a position tuple, we can retrieve the x and    x, y = pt      or  x = pt[0]
y coordinates using:                                                       y = py[1]

For example, to calculate the distance of pt from the origin we could write:

dist = math.sgrt(pt[0] ** 2 + pt[1] ** 2)

Now this is not very readable, and if someone sees this code they will have ti know thatpt[0] mans the x-coordinate and pt[1] means the y-coordinate.

This is not very transparent.



            # Using a class instead.
At this point, in order to make things clearer for the reader (not the complier, the reader), we might want to approach this using a class method instead.

"""
from calendar import month
import symbol


class Point2D:
    def __init__(self, x, y):           # pt = Point2D(10, 20)
        self.x = x
        self.y = y


class Stock:
    def --init__(self, symbol, year, month, day, open, high, low, close):
        self.symbol = symbol
        self.year = year
        self.month = month
        self.day = day          # Class approach            # Tuple Approach
        self.open               # djia.symbol               # djia[0]
        self.high               # djia.open                 # djia[4]
        self.low = low          # djia.close                # djia[7]
        self. close = close
                                # djia.high - djia.low      # djia[5] - djia[6]


"""         Extra stuff
At the very least we shouldimpliment the __eq__ method too
    -> Point(10, 20) == Point(10, 20)  ->  True

"""

class Point2D:
    def __init__(self, x, y):           # pt = Point2D(10, 20)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y}'

    def __eq_(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        else:
            return False


"""         Named Tuples to the rescue
There are other reasons to seek another approach, We cover those in the coding video

Amonst other thing, Point2D objects are mutable - something we may not want!

There's a lot to like using tuples to represent simple data structures

The real drawback is that we have to know what the positions mean, and remember this in our code.

If we ever need to change the structure of our tuple in our code (like inserting a value that we forgot) and most likely our code will break!




        Named Tuples to the rescue

Named tuples give meaningful name to positions:
    They subclass tuple, and add a layer to assign property names to the positional elements

Located in the collections standard library module
    from collections import nametuple

        named tuple is a function (not a type) which generates a new class      -> class factory
                that new class inherits from tuple
                but also provides named properties to access elements of the tuple
                but an instance of that class is still a tuple



        Generating Named Tuple Classes

We have to understand that namedtuple is a class factory

namedtuple needs a few things to  generate this class:
    the class name we want to use
    a sequence of field names (strings) we want to assign, in the order of the elements in the tuple
        field names can be any valid variable name
        except they cannot start with an underscore

The return value of the call to namedtuple will be a class

We need to assign that class to a variable name in our code so we can use it to construct instances
n general, we use the same name as the name of the class that was generated

Point2D = namedtuple('Point2D', ['x', 'y'])

We can create instances of Point2D just as we would with anny class (since it is a class)
Pt2D = namedTuple('Point2D', ['x', 'y'])
pt = Point2D(19, 20)
                Variable:MyClass ---> Class: MyClass 0xFF300  # they point to the same memory object
class MyClass:                                /
    pass                                     /
                                            /
MyClassAlias = MyClass      Variable: MyClassAlias
instance_1 = MyClass()          instance_2 = MyClassAlias()     # instances of the same class

    Similarly
Pt2DAlias = namedtuple('Point2D', ['x', 'y'])
                                        | # Points to the same class
                                    Class:  )xFF900
    Variable: Pt2DAlias ------> Point2D

There are many ways we can provide the list of field names to the namedtuple function
    a list of strings      -> in fact any sequence, just remember that order matters!
    a tuple of strings     -> in fact any sequence, just remember that order matters!
    a single string with the field names seperated by whitespace or commas

namedtuple( 'Point2D', ['x', 'y'])

namedtuple( 'Point2D', ('x', 'y'))

namedtuple( 'Point2D', 'x, y')

namedtuple( 'Point2D', 'x y')



        Instantiating Named Tuples

After we have created a named tuple class, we can instanciate them just like an ordinary class

In fact, the __new__ method of the generated class uses the field names we provided as parm names

    Point2D = namedtuple( 'Point2D', ' x y')

Once we have created a class, I can use positional arguments:

    pt1 = Point2D(10, 20)       10 -> x     20 -> y

And even keyword arguments:
    pt2 = Point2D(x=10, y=20)       "           "



        Accessing Data in a named tuple

Since named tuples are  also regular tuples. we can still handle them just like any other tuple
    by index
    slicing
    iterate

Point2D = namedtuple( 'Point2D', 'x y')

pt1 = Point2D(10, 20)           isinstance(pt1, tuple) -> True

        x, y = pt1      # unpacking

        x = pt1[0]

        for e in pt1:   # iterate
            print(e)

But now, in addition, we can alos access the data using the field names:

Point2D = namedtuple( 'Point2D, 'x y')
pt1 = Point2D(10, 20)


pt1.x  -> 10

pt1.y  -> 20

Since nametuple generated classes inherit from tuple    class Point2D(tuple):
                                                            ...

pt1 is a tuple, and is therefore immutable

pt1.x = 100     will not work!



        The rename keyword-only argument for namedtuple

Remember that field names for named tuples must be valid identifiers but cannot start with a underscore
This will NOT work!!!   Person = namedtuple( 'Person), 'named age, _ssn')

nametuple has a keywordonly argument,rename     (defaults to False)     that will automatically rename any invalid field name

uses convention:    _{position in list of field names}

This will not work:
Person = namedtuple('Person', 'name age _ssn', rename=True)

And the actual field names would be:        name    age     _2



        Introspection

We can easily find out the field names in a named tuple generated class

class property -> _fields

person = namedtuple( 'Person', 'name age _snn', rename=True)

Person._fields      -> ('name', 'age', '_2')

Remember that namedtuple is a class factory, i.e. it generates a class
We can actually see what the code for that class is, using the class

"""

