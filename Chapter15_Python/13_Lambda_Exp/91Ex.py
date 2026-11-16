def mul(a, b):
    return a * b

mul_l = lambda a, b: a * b
print(mul_l(3, 4))

def sum_three_num(a, b, c):
    return a + b + c


op_f = lambda a, b, c: a + b + c
print(op_f(3, 4, 5))

#Explain this lambda function in simple terms:
# A lambda function is a small anonymous function defined using the 'lambda' keyword.
# It can take any number of arguments but can only have one expression.