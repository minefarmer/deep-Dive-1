# main_usage  run.py
import timing

code = '[x**2 for x in range(1_000_000)]'

result = timing.timeit(code, 100)
print(result)  # loading timing
Timing(repeats=100, elapsed=32.2464178, average=0.32246417800000005)
