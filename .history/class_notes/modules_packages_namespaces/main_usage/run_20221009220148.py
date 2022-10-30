# main_usage  run.py
import timing

code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100)
print(result)  # loading timing
            Timing(repeats=100, elapsed=0.02844229999999999, average=0.0002844229999999999)
