#lambda sample
#definition of lambda function - it is an anonymous function that can take any number of arguments, but can only have one expression.

def add(x, y):
    return x + y

print(add(5, 3))

add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))
