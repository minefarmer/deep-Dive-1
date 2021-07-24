'''             Modifying and extending Named Tuples

            Named tuples are immutable
How we can change values inside the tuple
Just like with strings, we have to create a new tuple, with the modified values

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(0, 0)  # will not work

Suppose we need to change the value of the x coordinate:
    Simple approach:  pt = Point2P(100, pt.y)
        Note: the memory address of pt has now changed
            This approach can work well, but it has a major drawback

Stock = namedtuple('Stock", 'symbol year month day open high low close')
djia = Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393)

Maybe slicing or unpacking?

djia = Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393)

current = djia[:7]  current -> djia - Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260)

*current, _ = djia djia - Stock['DJIA', 2021, 7, 23, 26313, 26458, 26260]

djia = Stock(*current, 26394)


I can also use the _make class method - but we need to create an iterable that contains all the values first:

    new_values = current + (26394,)     new_values = current.append(26394)

    new_ values -> 'DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393, 26394

                        / iterable
djia = stock._make(new_values)


This still has drawbacks
djia = Stock('DJIA', 2021, 7, 23, 26313, 26458, 26260, 26393)

What if we wanted to change the value in the middle     i.e.(day)
        *pre, day, *post = djia  # makes no sense...


Slicing will work:  pre = djia[:3]
                    post = djia[4:]

new_values = pre + (26,) + post

new values -> ('DJIA', 2021, 7, 26, 26313, 26458, 26260, 26393)

djia = Stock(*new_values)


But even this has some draw backs!

'''