"""Import Variants and some misconceptions
# module1.py
import math
                                    sys.modules
is math in sys.modules?               math   <module object>  ________
    if not, load and insert ref                                         \
                                                                         \
add symbol math to module1's global namespace referencing the same object \
                                                                          /
                                                                        /
                                                                       /
                                        module`.globals()             /
                                            math    <module object>__/
                                                                        math symbol in namespace

(if math symbol already exists in module1's namespace, replace reference)



Import variants

#  module1.py
add symbol r_math       sys.modules
                            math    <module object>____________
                                                                \
                                                                \
is math in sys.modules?                                           \
    jf not, load it and insert ref                                  \
                                                                    
add symbol r_math to module1's global namespace refering the same object

                module1.globals()
                  r_math    <module object>

                                            r_math  <module object>

                                                                    r_math symbol in namespace

(if math symbol already exists in module1's namespace, replace reference)

"""