"""[Default values]
What happens at run time...
    When modules are loaded:  All the code is executed immediately.

        Module Code

        a = 10          the interger object 10 is created and a references it.

        def func(a):    the function object is created, and func references it.
            print(a)

        func(a)         the function is executed


What about default values?

    Module code

    def func(a=10):     the function object is created, and func references it
        print(a)        the integer object 10 is evaluated/created and is assigned as the default value for a


    func()              the function is executed

                        by the time this happens, the default value for a has already been evaluated and assigned - it is not re-evaluated when the function is called


So what?

Consider this:

We want to create a function that will write a log entry to the console with a user-specified event date/time. If the user does not supply a date/time, we want to set it to the current date/time.

from datetime import datetime

def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

log('message 1')    -> 2017-08-21 20:54:37.706994 : message 1
    a few minutes later
log('message 2')    -> 2017-08-21 20:54:37.706994 : message 3   ## note the same time is shown above.

Solution Pattern = need to show current time it was executed

    We set a default for dt to None

    If dt is None, set it to current date/time

    otherwise, use what the caller specified for datetime


        from datetime import datetime

        def log(msg, *, dt=None):
            print ('{0}: {1})

"""