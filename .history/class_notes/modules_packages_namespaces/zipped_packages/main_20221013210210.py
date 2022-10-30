# package imports: main.py
import common
import common.validators as validators
import common.modules as models
# from common.modules import *
import common.helpers as helpers


validators.is_boolean('true')
validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('2022-1013')

john_post = models.Post()
john_posts = models.Posts()
john = modules.User()


print('\n\n***** self *****')
for k in globals().keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

print('\n\n***** numeric *****')
for k in common.validators.numeric.__dict__.keys():
    print(k)






# >>> import sys
# >>> sys.path
# ['', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\\python39.zip', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\\DLLs', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\\lib', 'C:\\Users\\pgold\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0', 'C:\\Users\\pgold\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages', 'C:\\Users\\pgold\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\win32', 'C:\\Users\\pgold\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\win32\\lib', 'C:\\Users\\pgold\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\Pythonwin', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\\lib\\site-packages']
# >>> 
