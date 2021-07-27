from pprint import pprint

print('----------- Running {0}  --------'.format(__name__))

def pprint_dict(header, d):
    print('\n\n-----------------')
    print('****** {0} *****'.format(header))
    for key, value in d.items():
        (key, value)
    print('----------------------\n\n')

pprint_dict('module1.globals', globals())

print('---------- End of {0} ------------',format(__name__))  # ----------- Running __main__  --------


                                                    # -----------------
                                                    # ****** module1.globals *****
                                                    # ----------------------


                                                    # ---------- End of {0} ------------ __main__
                                                    # ---------- End of __main__ -------------














# from pprint import pprint


# print('------- Running {0} -----------'.format(__name__))
# def pprint_dict(header, d):
#     print('****** {0} *****'.format(header))
#     for key, value in d.items():
#         print(key, value)
#     print('------------------------------\n\n')


# pprint_dict('module1.globals', globals())

print('---------- End of {0} -------------'.format(__name__))  ----------- Running __main__  --------


-----------------
****** module1.globals *****
----------------------


---------- End of {0} ------------ __main__
---------- End of __main__ -------------


