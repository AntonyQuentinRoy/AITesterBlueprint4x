a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    result = a / b
    print("The result of division is: ", result)
except (ZeroDivisionError, ValueError , TypeError):
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution completed.")

