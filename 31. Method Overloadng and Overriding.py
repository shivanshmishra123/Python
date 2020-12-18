"""Overriding occurs when a derived class or child class has the same method that has already been
defined in the base or parent class. Being the same methods with the same name and number of parameters,
when called checks for the method first in a child class, and runs it ignoring the method in the parent
class because it is already overridden. In the case of Instance variables, the case is a little different.
When the method is called, the program will look for any instance variable having the same name as the 
one that is called in the child, then in the parent, and after that, it comes again into child class if
not found.

"""

# Accha tha isliye chhap dala poora paragraph 

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)

