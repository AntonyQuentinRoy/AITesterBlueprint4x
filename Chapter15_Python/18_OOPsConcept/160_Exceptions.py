#Exception Handling in Python
"""
Exceptions are errors that occur during the execution of a program. 
When an exception occurs, the normal flow of the program is interrupted,
and Python generates an error message.
To handle exceptions and prevent the program from crashing, 
we can use exception handling techniques.
"""
# Sample code for exception handling in Python:

# try:
#     # Code that may raise an exception
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Please enter valid integers.")
# except Exception as e:
#     print("An unexpected error occurred:", e)
# else:
#     print("No exceptions occurred. The program executed successfully.")
# finally:
#     print("Execution completed.")

print(a)
#Name error: name 'a' is not defined

print(10/0)
#ZeroDivisionError: division by zero
