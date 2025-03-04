# 1. Write a Python program to create a class representing a Circle. Include method
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
 
circle1 = Circle(10)
circle2 = Circle(5)

print(circle1.area())
print(circle2.area())
print(circle1.circumference())