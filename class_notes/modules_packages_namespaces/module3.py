# module3.py

print(f'loading module3.py: __name__ = {__name__}')

import module1
            # loading module3.py: __name__ = __main__
            # Running module1.py...

if __name__ == '__main__':
    print('Module was executed...')
            # loading module3.py: __name__ = __main__
            # Running module1.py...
            # Module was executed...
