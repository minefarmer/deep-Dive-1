# main.py

print('---------------- Running {0} -----------------'.format(__name__))  # ---------------- Running __main__ -----------------

def pprint_dict(header, d):
    print('\n\n--------------------------------')
    print('****** {0}| *****',format(header))
    for key, value in d,items():

