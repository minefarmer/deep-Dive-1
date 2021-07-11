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

There is no concept of a truly global (across all the modules in our app) scope in Python

The only exception to this are some of the built=in globally available objects, such as:
    True    False   None    dict    print


The built-in global variables can be used anywhere inside our module

    including inside any function

Global scopes are nested inside the built-in scope

                                Built-in Scope
            Module 1                               name spaces
            Scope   name                        var1    0xA345E
                    space                       func1   0xFF34A

                    Module 2
                    Scope   name
                            space

If I reference a variable name inside a scope and Python does ot find it in that scope's namespace


        Examples

module1.py      Python does not find True or print in the current (module/global) scope

print(True)     So, it looks for them in the enclosing scope -> build-in
                Finds them there  -> True


module2.py      Python does not find a or print in the current (module/global) scope

print(a)        So, it looks for them in the enclosing scope    -> built-in

                Find print, but not a   -> run-time Name Error


module3.py
print = lambda x:  'hello {0}!'.format(x)

s = print('world')      Python finds print in the module scope
                        So it uses it
                        s -> hello world




            The Local Scope

When we create functions, we can create variable names inside those functions (using assignments)
    e.g. a = 10

Variables defined inside a function qre not created until the function is called

Every time the function is called, a new scope is created
    Variables defined inside the function are assigned to the scope     -> Function Local scope
                                                                        -> Local scope

    The actual object the variable references could be different each time the function is called

    (this is why recursion works!)


        Examples
                    my_func
def my_func(a,b):    a
    c = a * b         b
    return c           c

                    my_func
my_func('z', 2)     a-> 'z'
                       b->2
                        c->'zz' \
                                same names, different local scopes
                    my_func     /
my_func(10, 5)      a->10
                      b->5
                        c->50




            Nested scopes

Module scopes are often nested inside Built-in scopes

Local are inside of built-in scopes.

Python looks first at the local scope, then at the Module scope and then the built-in scope

When I call a function a second time, a new local scope is created


        Name space lookups

When requesting the object bound to a variable name:
    e.g. print(a)  # don't worry about "print"

Python will try to find the object bound to the variable

Python will try to find the object bound to the variable  # a
    in the current local scope first
    works up the chain of enclosing scopes

When my_func (var) finishes running, the scope is gone too!
    and the reference count of the object var was bound to (referenced) and is decremented

We say that var goes out of scope


        Accessing the global scope from the local scope

When retrieving the value of a global variable from inside a function, Python automatically searches the local scope's namespace, and up the chain of all the enclosing scope namespaces

    local   -> global   -> built-in

Modifying a global variables value from inside the function

a = 0
                  assignment -> Python interprets this as a local variable (at compile-time)>
                                ->The local variable (a) masks the global variable a

                    />assignment  -> Python interprets this as a local variable variable (at compile-time)
                                -> the local variable a masks the global variable a
def my_func():   /
    a = 100    </
    print(a)

my_func()   # 100

print(a)  # 0


        The global keyword

We can tell Python that a variable is meant to be scoped in the global scope by using the global keyword

a = 0

def my_func():
    global a
    a = 100

my_func()

print(a)  # 100     # It is printing the global a, which was made 100 by def my_func

"""