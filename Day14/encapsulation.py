######## Encapsulation
# Bundling of data(attribute) and methods (functions) within a class, restricting access

# Types of encapsulation
# 1. Public Members: Accessible from anywhere
# 2. Protected Members: Accessible withing the class and it's subclass
# 3. Private Members: Accessible only within class

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def display(self):
        """Method to display the details"""
        print(f"Name is {self.name}, Salary:{self.__salary}")

    def get_salary(self):
        return self.__salary

person = Person("Alice", 30, 50000)
print(person)
# print(person.__salary) # this will raise an attribute error
print(person._age)
print(person.get_salary())

############ Abstraction --> hiding the implementation and exposing only the necessary part
# of the object
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        # return super().speak()
        print("woof")

dog = Dog()
dog.speak()

############ Inheritance
# Types of Inheritance
# 1. Single inheritance --> one child class inherits from one parent

class Person:
    pass

class Child(Person):
    pass

# 2. Multiple inheritance --> child class inherits from more than one parent
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass

# 3. Multilevel inheritance --> child class inherits from a parent, which in turn inherits from another parent

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

# 4. Hierarchical inheritance --> more than one child class inherits from a parent class

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# 5. Hybrid inheritance --> combination of two or more types of inheritance

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class Derived3(Derived1, Derived2):
    pass


######################################## 
# 2. Multiple inheritance 
class Parent1:
    pass
class Parent2:
    pass

class child(Parent1, Parent2):
    pass

# 3. Multilevel inheritance
class GrandParent1:
    pass

class Parent1(GrandParent1):
    pass

class Child1(Parent1):
    pass

# 4. Hierarchical inheritance
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# 5. Hybrid inheritance
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class GrandChild(Child1, Child2):
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Sound from parent")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        super().make_sound()

    def make_sound(self):
        print("Sound from child")

dog = Dog("Tom", "Rottweiller")
print(dog.name)
print(dog.breed)

