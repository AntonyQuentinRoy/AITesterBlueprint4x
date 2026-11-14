#OOPs concepts in python
#Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. Python supports OOP and provides features like encapsulation, inheritance, and polymorphism.
#Abstraction: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. In Python, abstraction can be achieved using abstract classes and interfaces.
#Encapsulation: Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, called a class. In Python, encapsulation is achieved by using access modifiers (public, private, protected) to control the visibility of class members.
#Inheritance: Inheritance is the mechanism by which one class can inherit properties and behaviors from another class. In Python, a class can inherit from another class using the syntax `class ChildClass(ParentClass):`.
#Polymorphism: Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. In Python, polymorphism can be achieved through method overriding and operator overloading.

#Class definition
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")