# run.py 
import timing

code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100)
print(result)  # loading timing...
                # Timing(repeats=100, elapsed=0.044259999999999994, average=0.0004425999999999999)


# print(f'loading run.py: ++name__ = {__name__}')  # loading run.py: ++name__ = __main__
#                                                 # Loading module1.py: __name__ = module1


# import module1