# run.py
import timing

code = '[x**2 for x in range(1_000_000)]'
print(code)
result = timing.timeit(code, 100)
print(result)  # Timing(repeats=100, total=0.02491102400017553, average=0.0002491102400017553)
               # Timing(repeats=100, total=19.631679865000024, average=0.19631679865000023)

# print(f'loading run.py: __name__ = {__name__}')  # loading run.py: __name__ = __main__
