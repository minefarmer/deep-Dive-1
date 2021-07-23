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
        self.low = low          # djia.close
        self. close = close


