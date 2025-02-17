# 1. Compile time polymorphism (Method Overloading)

class Math:
    def add(self, a, b, c=0):
        return a + b + c
    
math = Math()
print(math.add(2, 3, 9))

## just an example for taking multiple arguments
class Math:
    def add(self, **args):
        return sum(args)
    

# 2. Runtime polymorphism (Method overriding)

class Animal:
    def make_sound(self):
        return "some sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
class Cat(Animal):
    def make_sound(self):
        return "Meouw"

animal = Dog()
print(animal.make_sound())


