"""                     Global and local Scopes

            Scopes and Namespaces

When an object is assigned to a variable    # a = 10

    that variable points to some object

        and we say that the variable (name) is bound to that object

That object can be accessed using that name in various parts of our code

# ###   I can't reference that (a) just anywhere in my code!

That variable name and it's binding (name and object) only "exist" in specific parts of our code

    The porton of code where that name/binding is defined, is called the lexical scope of the variable

    These bindings are stored in namespaces

    (each scope has its own namespace)




            The global scope

The global scope is essentially the module scope

It spans a single file only

"""