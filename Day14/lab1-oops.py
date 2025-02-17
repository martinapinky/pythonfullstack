# Create an abstract class Device with an abstract method turn_on().
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# Derive Smartphone and Laptop classes from it and implement the turn_on() method.
class SmartPhone(Device):
    def turn_on(self):
        return "Smart phone turned on"

class Laptop(Device):
    def turn_on(self):
        return "Laptop turned on"

smart_phone = SmartPhone()
laptop = Laptop()
print(smart_phone.turn_on())
print(laptop.turn_on())
# Create a BankAccount class with a private attribute _balance.
# Implement methods deposit(), withdraw(), and get_balance() to modify and access _balance.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"{amount} Deposited Successfully!"

    def withdraw(self, amount):
        self.__balance -= amount
        return f"{amount} Withdrawn Successfully!"
  
    def get_balance(self):
        return self.__balance

my_account = BankAccount(10000)
print(my_account.deposit(2000))
print(my_account.withdraw(1000))
print(my_account.get_balance())

# Create a Bird class with a method make_sound().
# Derive Parrot and Sparrow classes that override make_sound() with their own implementation.
# Create a function play_sound() that takes a Bird object and calls its make_sound() method.
class Bird:
    def make_sound(self):
        return "Some sound"

class Parrot(Bird):
    def make_sound(self):
        return "Parrot sound"

class Sparrow(Bird):
    def make_sound(self):
        return "Sparrow sound"

bird = Bird()
parrot = Parrot()
sparrow = Sparrow()
print(bird.make_sound())
print(parrot.make_sound())
print(sparrow.make_sound())

# Create an abstract class Vehicle with private attributes _speed and _fuel.
# Implement a method drive() and create subclasses Car and Bike to define how they are driven.
class Vehicle(ABC):
    def __init__(self, speed, fuel):
        self.__speed = speed
        self.__fuel = fuel

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        self.__speed = speed
        self.__fuel = fuel

    def drive(self):
        if self.__fuel > 0:
            return f"The car is driving at {self.__speed}"
    
class Bike(Vehicle):
    def __init__(self, speed, fuel):
        self.__speed = speed
        self.__fuel = fuel

    def drive(self):
        if self.__fuel > 0:
            return f"The bike is driving at {self.__speed}"
    
car = Car(100, 50)
bike = Bike(50, 30)
print(car.drive())
print(bike.drive())