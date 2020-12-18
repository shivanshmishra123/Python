# Two types :- Instance Variable and Class Variables
# Arre bhai jo humne tutorial #25 mei seekha tha wo instance variables the jaise
# student1.age = 55

# Class Variables 
"""
Ese variable jo Class ke paas ho jaise agar mere paas employee class hai to agar sabko jo 
no of chuttiya hai wo same mil rhi hai wo same hai to mai usse harry.noofleaves and larry.noofleaves
ke bajaye seedhe Employee class ke under likh skta hai 
"""

# Note :- Isko mai access to kr skta hu harry.noofleaves ya larry.noofleaves se lekin isse change sirf
# Employee.noofleaves se hi skta hu 
#Example :-

class Employee():
    noofleaves = 8
    """
    docstring
    """
    pass

harry = Employee()
larry =Employee()

harry.name = "Harry"
harry.salary = "8000"
harry.role = "Programmer"


larry.name = "Larry"
larry.salary = "6000"
larry.role = "Accountant"

print(harry.noofleaves)
print(larry.noofleaves)
print(Employee.noofleaves)

Employee.noofleaves = 10
print(harry.noofleaves)