import time
# https://www.epochconverter.com/
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
    return wrapper

def print_logs(func):
    def wrapper():
        print("Start the logs")
        func()
        print("End of the log")
    return wrapper


@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)


def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)

print(" -----  ")
#with decor
test_ui_1()

print(" -----  ")
# without the decor
test_ui_2()

#Explain this program flow in simple terms:
# Step1: The program starts by importing the 'time' module,
# which is used to measure the execution time of functions.

# Step2: A decorator function 'time_decorator' is defined,
# which takes another function as an argument.
# Inside this decorator, a wrapper function is defined that records the start time,
# calls the original function, records the end time, and then calculates 
# and prints the total time taken by the function.