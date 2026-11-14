#Decorators meaning - A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

import time
import functools

def time_decorator(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

#with decorator
@time_decorator
@print_logs
def ui_test1():
    print("UI Test 1 executed")
    time.sleep(2)

#without decorator
def ui_test2():
    print("UI Test 2 executed")
    time.sleep(2)


ui_test1()
ui_test2()