"""                         Importing modules
When we run a statement such as
    import fractions
    what is python doing

The first thing to note is that Python is doing the import at run time, i.e. while my code is actually running
This is differient from traditional compiled languages such as C, where modules are compiled and linked at compile time
In both cases though, the system needs to know where those code files exist
Python uses a relatively complex system of how to find and load modules. I'm not going to even attempt to describe this in detail, but we'll take a brief look at the main points
The sys module has a few properties that define where Python is going to look for modules (either built-in or standard library as well as our own or third party):
    import sys


"""