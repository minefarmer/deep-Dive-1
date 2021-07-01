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

def func(a, b, *args, d):
    # code

In this case, *args effectively exhausts all positional arguments
    and d must b passed as a keyword (named) argument

func(1, 2, 'x, 'y' d = 100)
        -> a = 1, b = 2, args = ('x', 'y'), d = 100

func(1, 2, d= 100)
    ->  a = 1, b = 2, args = (), d = 100

func(1, 2)  ## will fail because python could not find d

            [I can omit any mandatory arguments:]

def func(^args, d)

'''