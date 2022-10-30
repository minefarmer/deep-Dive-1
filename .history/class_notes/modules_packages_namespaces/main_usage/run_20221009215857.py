# main_usage  run.py
import timing

code = '[x**2 for x in range(1_000)]'

result = timing.runtimit(code, 100)
