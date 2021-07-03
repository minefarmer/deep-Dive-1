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


"""