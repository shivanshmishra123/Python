"""
Private Variable - Only classes allowed can access
Protected Variable - Only  allowed classes can access it
Public Variable - All classes can access it.
"""

# Public Variable
# Declaration = Normal tareeke se 
# Example
class Employee():
    noofleaves = 10 #This is a public variable
    """
    This class is all about Employee of a company 
    """
    pass

Employee1= Employee()
Employee2= Employee()

Employee1.noofleaves = 5 
print(Employee1.noofleaves)


# Protected Variable
# Declaration = _variablename
# Acceessig it = print Instance or class name._variable name (_lagane ki zaroorat  hai)
# Example

class Employee():
    _noofleaves = 10 #This is a protected variable
    """
    This class is all about Employee of a company 
    """
    pass

Employee1= Employee()
Employee2= Employee()
print(Employee1._noofleaves)

# Private Variable
# Declaration = __variablename
# Acceessig it = print(Instance or class name._Classname__variable name) (__lagane ki zaroorat  hai)
# Example

class Employee():
    __noofleaves = 10 #This is a protected variable
    """
    This class is all about Employee of a company 
    """
    pass

Employee1= Employee()
Employee2= Employee()
print(Employee1._Employee__noofleaves)