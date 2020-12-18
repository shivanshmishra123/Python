"""
Kabhi Kabhi jab hume kisi fuction ko har child class mei rkhna compulsory krna ho to hum abstractmethod
ka use krte hai .... In the given example below the printarea function is a abstract method
"""

from abc import ABC, abstractmethod

class Shape(ABC): #Parent class mei ABC krna zaroori hai 
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())


