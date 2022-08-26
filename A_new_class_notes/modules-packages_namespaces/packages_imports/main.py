# package imports  main.py
import common
import common.validators as validators
<<<<<<< HEAD:class_notes/modules_packages_namespaces/packages/package_imports/main.py
import common
# import common.models.post.post
# import common.models.post.posts
# import common.models.users.user
=======
import common.models.posts.post
import common.models.posts.posts
import common.models.users.user
>>>>>>> 086fa1eced0224d54163ef47a4f6e47e55ecb36e:A_new_class_notes/modules-packages_namespaces/packages_imports/main.py


<<<<<<< HEAD:class_notes/modules_packages_namespaces/packages/package_imports/main.py
john_post = common.models.posts.post.Post()
john_post = common.models.posts.posts.Posts()
john = common.modules.users.user.User()
=======
# validators.is_boolean('true')
# validators.is_json('{}')
# validators.is_numeric(10)
# validators.is_date('2022-08-25')
>>>>>>> 086fa1eced0224d54163ef47a4f6e47e55ecb36e:A_new_class_notes/modules-packages_namespaces/packages_imports/main.py

john_post = common.models.post.post.Post()
john_posts = common.models.posts.posts.Posts()

john = common.models.users.user.Users()


print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** self *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __annotations__
            # __builtins__
            # __file__
            # __cached__
            # common



print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)  # ***** common *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # validators


<<<<<<< HEAD:class_notes/modules_packages_namespaces/packages/package_imports/main.py
# print('\n\n***** validators *****')
# for k in common.validators.__dict__.keys():
#     print(k)  # ****** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric



=======
>>>>>>> 086fa1eced0224d54163ef47a4f6e47e55ecb36e:A_new_class_notes/modules-packages_namespaces/packages_imports/main.py


print('\n\n***** models *****')
for k in common.models.__dict__.keys():
    print(k)  # ***** models *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__




# print('\n\n***** validators *****')
# for k in common.validators.__dict__.keys():
#     print(k)  # ***** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric


<<<<<<< HEAD:class_notes/modules_packages_namespaces/packages/package_imports/main.py
=======

>>>>>>> 086fa1eced0224d54163ef47a4f6e47e55ecb36e:A_new_class_notes/modules-packages_namespaces/packages_imports/main.py
# print('\n\n***** numeric *****')
# for k in common.validators.numeric.__dict__.keys():
#     print(k)  # ***** numeric *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __file__
            # __cached__
            # __builtins__
            # is_interger
            # is_numeric
            # numeric_helper_1
            # numeric_helper_2
