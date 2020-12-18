# Operator Overloading
"""
Jis tarah + symbol ka meaning 2 no and 2 strings ke liye differents hota hai to usko hum bolte hai 
That it is working differently in those to scenarios.... 

In the same way defining a method for a operator is known as operator overriding
"""

# Dunder Methods
"""
The methods which are used for Operator Overloading are called method overloading

Methods starting with a double underscore ( __ ) and ending with a double underscore
( __ ) represents dunder methods.
"""


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    # def __repr__(self):
    #     return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    # def __str__(self):
    #     return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")
__add__(emp1,emp2)
