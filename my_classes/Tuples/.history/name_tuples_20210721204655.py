"""             Tuple as Data Structure
We have see how we interpreted tuples as data structures

The position of the object contained in the tuple gives it meaning

For example, we can represent a 2D coordinate as: (10, 20)
                                                    x   y

If pt is a position tuple, we can retrieve the x and    x, y = pt      or  x = pt[0]
y coordinates using:                                                       y = py[1]

For example, to calculate the distance of pt from the origin we could write:

dist = math.sgrt(pt[0] ** 2 + pt[1] ** 2)

Now this is not very readable, and if someone sees this code they will have ti know thatpt

"""