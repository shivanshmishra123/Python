# There are basically three types of methods
# 1. Instance Method 2.Class method 3.Static methods

# Instance Method
# Jab bhi hume kisi method(function) ki madat se apne kisi Instance ko value assign krni ho to hum 
# iska use krte hai

# Syntax : - We use __init__ to call it 
# Example:-
class Employee():
    """
    docstring
    """
    pass

    def printdetails(self):
        print(f"The name is {self.name}, Salary is {self.salary} and the role is {self.role}")
    
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

harry = Employee("Harry","8000","Programmer")
larry = Employee("Larry","6000","Accountant")

harry.printdetails()
print(larry.name)

# Class Method
# Jab bhi hume kisi method ki madat se apne class variable ko vaue assign krni ho to hum 
# iska use krte hai aur iska use tab bhi hota hai jab hume instance ko bhi class variable 
# ka access dena ho 
# Syntax : - @classmethod se isko pehle define krna hota hai 
# Example:-
class Employee():
    """
    docstring
    """ 
    leaves = 8 
    pass

    def printdetails(self):
        print(f"The name is {self.name}, Salary is {self.salary} and the role is {self.role}")
    
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def change_no_of_leaves(cls,newleaves):
        leaves = newleaves

harry = Employee("Harry","8000","Programmer")
larry = Employee("Larry","6000","Accountant")

Employee.change_no_of_leaves(5)
print(Employee.leaves)

# # Static Method
# # Jab bhi hume kisi method ko ese hi normally hi bas banana ho to iska use hota hai

# # Syntax:- @staticmethod se isko pehle define krna hota hai 
# # Example:-
# class Employee():
#     """
#     docstring
#     """
#     pass

#     @staticmethod
#     def name(str1):
#         str1 = input("Enter the No.")
#         print(f"Hi {str1}!! Now you are a part of coding community")
#     name()




