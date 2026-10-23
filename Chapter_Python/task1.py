#### Take 2 inputs from user and perform addition of 2 numbers,subratction,multiplication and 
#### division of 2 numbers,print quotient and remainder of 2 numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("ADDITION The sum is: " + str(number1 + number2))
print("SUBTRACTION The difference is: " + str(number1 - number2))
print("MULTIPLICATION The product is: " + str(number1 * number2))
print("DIVISION value: " + str(round(number1 / number2, 1)))
print("QUOTIENT is: " + str(round(number1 / number2, 1)))
print("REMAINDER is: " + str(round(number1 % number2, 1)))