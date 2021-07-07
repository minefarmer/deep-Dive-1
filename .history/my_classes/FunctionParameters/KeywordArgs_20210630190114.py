'''         [Keyword Arguments]
Positional parameters can, optionally be passed as named (keyword) arguments

def func(a, b, c):
    # code

func(1, 2, 3)           -> a = 1, b = 2, c = 3

func(a=1, c=3, b=2)         -> a = 1, b = 2, c = 3


Using named arguments in this case is entirely up to the caller.


            [Mandatory Keyword Arguments]

I can make keyword arguments mandatory
to do so, I can create parameters after the positional parameters have been exhausted

def func(a, b, ^args, d):
    # code

In this case, *args effectively exhausts all positional arguments
    and d must b passed as a keyword (named) argument

func(1, 2, 'x, 'y' d = 100)
        _. a = 1, b = 2, args = ()

'''