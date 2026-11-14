class Calc:
    a = 10
    b = 20

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b

a = float(input("Enter a: "))
b = float(input("Enter b: "))
calc = Calc(a, b)
print("Addition:", calc.add())
print("Subtraction:", calc.sub())
print("Multiplication:", calc.mul())