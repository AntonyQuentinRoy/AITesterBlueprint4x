from symtable import Class


class Person:
    # Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    # Behavriour
    def talk(self):  # self - this , self will be first argument in every behaviour.
        print("I can Talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def method_walk_return(self):  # No Arg with Return
        return "I am walking"



def function_outside():
    print("Outside")


geeta = Person()
amit = Person()
navita = Person()


#Constructor

class Mobile:
    def __init__(self, brand, model, price):  # Constructor
        self.brand = brand
        self.model = model
        self.price = price

    def show(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

        iphone = Mobile("Apple", "iPhone 14", 100000)

        #self is used to refer to the current instance of the class. It allows you to access the attributes and methods of the class within its own methods. In the constructor, self.brand, self.model, and self.price are used to assign values to the instance variables of the Mobile class.
        #self is equal to this in Java. It is a reference to the current object being created or manipulated.

       
