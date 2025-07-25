print("OOP in Python")

""" Class and Objects"""
print(" Class and Object")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Person Object
p1 = Person("Hassaan", 20)
print({"Age:": p1.age,"Name": p1.name})


"""Class variable and instance variable"""
print("\n#Class variable and instance variable")

class Student:
    University = "GCUF"     #class variable
    def __init__(self, name):
        self.name = name    #instance variable

s1 = Student("Hassaan")
print(s1.University, s1.name)



"""Method Types"""

# Static Method
class Demo:
    @staticmethod
    def static_method():
        print("Checking the instance method")


#Instance Method
class Demo2:

    def __init__(self, location):
        self.location = location


#class method
class Demo3:
    count = 5

    @classmethod
    def class_method(cls):
        print(cls.count)



"""Dunder Methods"""
print("\n#Dunder Methods")

class Books:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"

b = Books("Kite Runner")
print(b)

"""Pillars of Polymorphism"""
print("\n#Pillars of Polymorphism")

#Polymorphism
print("\n##Polymorphism")
class Pakistani:

    @staticmethod
    def say_hello():
        return "AssalamuAlaikum"

class American:

    @staticmethod
    def say_hello():
        return "Hello"

class Japanese:

    @staticmethod
    def say_hello():
        return "Konnichiwa"

people = [Pakistani(), American(), Japanese()]

for person in people:
    print(person.say_hello())


#Inheritance
print("\n##Inheritance")
class Animal:

    def cat(self):
        return "Meow"

class Dog(Animal):

    def dog(self):
        return "Bark"

d = Dog()
print(d.cat())
print(d.dog())

#Encapsulation

class Encapsulation:
    def __init__(self, name, grade, age):
        self._name = name       #protected
        self.__grade = grade    #private
        self.age = age          #public

# Abstraction
print("\n##Abstraction")
from datetime import datetime, timezone

print(datetime.now(timezone.utc))       #We know the working but not the logic of datetime library


"""Method Overriding"""
print("\nMethod Overriding")
class Father:

    @staticmethod
    def talk():
        print("Father.com :)")

class Son(Father):

    @staticmethod
    def talk():
        print("Beta.com :)")

s = Son()
s.talk()



