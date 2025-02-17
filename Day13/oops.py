# oops
# Class and Objects

# Class --> Blueprints --> set of attributes and methods
# Attribute are variables that belong to that class

class MyClass:
    x = 2  # attribute

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Method (behavior)
    def start_engine(self):
        return f"{self.brand} has started"
    def __str__(self):
        return f"{self.brand} and {self.model}"
    
# Create the objects of the class
car1 = Car("Ford", "Civic", 2020)
car2 = Car("Ford", "Model1", 2020)

print(car1)
print(car1.model)
print(car1.start_engine())

print(car1)


####### 4 Pillars
# Encapsulation --> bundle of attributes and methods. controlled access
# public protected private --> __balance  (name mangling)

# Inheritance --> inheriting from parent class

# Abstraction --> Hiding of the actual implementation

# Polymorphism --> same methods behaving differently
