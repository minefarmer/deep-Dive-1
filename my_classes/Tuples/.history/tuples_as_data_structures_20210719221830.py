"""             Tuples
Tuples are immutable
Tuples are more than read only lists

    Tuples                      Lists                   Strings
containers                  containers              containers
order matters               order matters           order matters
Heterogeneous/Homogeneous   Heterogeneous           Homogeneous
Indexable                   Indexable               Indexable
Iterable                    Iterable                Iterable
Immutable                   Mutable                 Immutable
    'fixed length'            'length can change'     'fixed length'
    'fixed order'           'order can change'        'fixed order'
can't do in-place sorts       Can do in place sorts
can't do in-place reversals.  Can do in place reversals



        Immutable tuples
elements cannot be added or removed
the order of elements cannot be changed
works well for representing Data Structures:

Point: (10, 20)     First element is the x coordinate
                    Second element is the y coordinate

Circle: (0, 0, 10)  First element is the x-coordinate of the center
                    Second element is the y-coordinate of the center
                    Third element is the radius

City:('London', 'UK', 8_780_000)    Third element is the population
                                    The position of the data has meaning



        Extracting data from Tuples
We can also use tuplr ulpacking

We actually know how to do this -- covrred iny the section on function arguments

new_york = ('New York', 'USA', 8_500_000)   # Packed three values into  a tuple

city, country, population = new_york
________________________
    unpacked tuple



        Dummy Variables
Used for tuple unpacking when we are only interested ia a subset of the data field
Suppose we are interested only in the city name and the population

"""