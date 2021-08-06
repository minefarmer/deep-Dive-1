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
                                            

"""