'''[*args]
Recall from iterable packing
a, b, c = (10, 2O, 30)      ->  A = 10      B = 20  C = 30
Something similar happens when positional arguments are passed to a function:

def func1(a, b, c):
    # CODE

func1(10, 20, 30)       ->  a = 10  b = 20    c = 30

Recall also:    a, b, *c = 10, 20, 'a', 'b'     -> a=10     b=20    c=['a', 'b']

Something similar happens when positional arguments are passed to a function:

def func1(a, b, *c):
    # code

func1(10, 20, 'a', 'b')     ->  

'''