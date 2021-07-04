"""[Lambda Expressions]
Lambda expressions are simply another way to create functions       anonymous functions

keyword \   parameter list optional
         \      \                the : is required, even for zero arguments
          \      \              /     / this expression is evaluated and returned when the lambda function is called. (think of it as "the body" of the function)
        lambda [parameter list]: expression
                \
                the expression returns a function object
                that evaluates and returns the expression when it is called


        Examples
"""
from tkinter import Y
from unittest import FunctionTestCase


lambda x: x**2

lambda x, y: x + y

lambda : 'hello'

lambda s: s[::-1].upper()


type(lambda x: x**2)    -> function

Note that these expressions are function objects, but are not "named"
        -> anonymous Functions

lambdas, 
