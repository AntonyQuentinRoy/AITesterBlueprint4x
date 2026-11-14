#sample function

def greet(name):
    print("Hello, " + name + "!")

greet("Antony")
#sample function with return value

#type1 function with no parameter and no return value
def greet():
    print("Hello, World!")

greet()

#type2 function with parameter and no return value
def greet(name):
    print("Hello, " + name + "!")

greet("Antony")

#type3 function with no parameter and return value
def greet():
    return "Hello, World!"

print(greet())

#type4 function with parameter and return value
def greet(name):
    return "Hello, " + name + "!"

print(greet("Antony"))

#type5 function with multiple parameters and return value
def greet(name, age):
    return "Hello, " + name + "! You are " + str(age) + " years old."

print(greet("Antony", 25))

#type6 function with default parameter value
def greet(name="World"):
    return "Hello, " + name + "!"

print(greet())
print(greet("Antony"))

#type7 function with variable number of parameters
def greet(*names):
    return "Hello, " + ", ".join(names) + "!"

print(greet("Antony", "John", "Doe"))

#type8 function with keyword parameters
def greet(**kwargs):
    return "Hello, " + ", ".join(kwargs.values()) + "!"

print(greet(name1="Antony", name2="John", name3="Doe"))

#type9 function with both positional and keyword parameters
def greet(name, **kwargs):
    return "Hello, " + name + "! " + ", ".join(kwargs.values()) + "!"

print(greet("Antony", name1="John", name2="Doe"))

#type10 function with both positional and variable number of parameters
def greet(name, *args):
    return "Hello, " + name + "! " + ", ".join(args) + "!"

print(greet("Antony", "John", "Doe"))

#type11 function with default parameter value
def greet(name="Antony", age=25):
    return "Hello, " + name + "! You are " + str(age) + " years old."

print(greet())

#user input function
def greet_user():
    name = input("What is your name? ")
    print("Hello, " + name + "!")

    greet_user()
