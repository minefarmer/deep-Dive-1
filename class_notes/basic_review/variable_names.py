'''     Identifier names

ARE case-sensitive  my_var  # these are all differient identifiers
                    my_Var
                    ham
                    Ham

    Must follow certain rules

start with a underscore(_) or letter(a-z, A-Z)
    followed by any number of underscores(_), letters(a-z A-Z), or digits(0-9)
        var     my_var    index1    index_1     _var    __var   __lt__      are all legal names
        
cannot be reserved words:
    None    True    False
    and     or      not
    if      else    elif
    for     while   break   continue    pass
    def     lambda  global  nonlocal    return  yield
    del     in      is      assert      class
    try     except  finally raise
    import  from    with    as

    
        Should follow certain conventions

Conventions

_my_var         This is a to indicate "internal  use" or "private"
|__             Objects named these way will not be imported by a statement such as:
|               from mobile import *
|__ single underscore


__my_var        Used to "mangle" lass attributes-useful in inheritance chains
|
|__ double underscore


__my_var__      Used for system defined names that have a special meaning to the interpreter.
|
|___double underscore   ## Dont invent them, stick to the ones pre-defined by python!

                            __init__
                            
                            x < y  ----> x.__init__(y)


Other naming conventions                    from the PEP 8 style guide

Packages    short, all-lowercase names. Preferbably no underscores.         utilities

Module      short, all-lowercase names. Can have underscores                db_utils    dbutils

Classes     CapWords (upper camel case) convention                          BankAccount

Functions   lowercase, words seperated by underscors (snacke_case)          open_account

Variables   lowercase, words seperated by underscores (snacke_case)         account_id

Constants   all-uppercase, words seperated by underscores                   MIN-APR

https:www.python.org/dev/peps/pep-0008/

'''