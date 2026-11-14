##Arithmetic Operators
a = input("Enter first number: ")
b = input("Enter second number: ")

if (a > b):
    print("a is greater than b")
elif (a < b):
    print("a is not greater than b")
else:
    print("a is equal to b")

c = 50
c += 1

d = 10
d += 2

print(c)
print(d)

input1 = input("Enter first number: \n")
input2 = input("Enter second number: \n")
input3 = input("Enter third number: \n")

if (input1 > input2) and (input1 > input3):
    print("input1 is greater than input2 and input3")
elif (input2 > input1) and (input2 > input3):
    print("input2 is greater than input1 and input3")
else:
    print("input3 is greater than input1 and input2")