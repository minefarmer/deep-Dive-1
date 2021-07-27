from pprint import pprint

print('----------- Running {0}  --------'.format(__name__))

def pprint_dict(header, d):
    print('\n\n-----------------')
    print('****** {0} *****'.format(header))
    for key, value in d.items():
        (key, value)
    print('----------------------\n\n')

pprint_dict('module1.globals', globals())

print('---------- End of {0} ------------',format(__name__))  #  /home/rich/anaconda3/envs/Matson/bin/python /home/rich/Desktop/carls_hub/deep-Dive-1/my_classes/ModulesPackages_PackageNamespaces/example1/module1.py
# ----------- Running __main__  --------


# -----------------
# ****** module1.globals *****
# ----------------------


# ---------- End of {0} ------------ __main__



