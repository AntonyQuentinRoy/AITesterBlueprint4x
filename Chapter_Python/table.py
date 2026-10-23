table = input("Enter a number: ")
print("The multiplication table of " + str(table) + " is: ")
for i in range(1, 11):
    print(str(table) + " x " + str(i) + " = " + str(int(table) * i))