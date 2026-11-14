#Class Sample
# from griffe import Class


# class Data:
#     #Attribute
#     attribute1 = "name"
#     attribute2 = 30
#     attribute3 = "New York"

#     def fun_inside(self, attribute1, attribute2, attribute3):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
#         self.attribute3 = attribute3


# def fun_outside(self):
#     print(f"Attribute 1: {self.attribute1}")
#     print(f"Attribute 2: {self.attribute2}")
#     print(f"Attribute 3: {self.attribute3}")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def get_age(self):
        return self.age
