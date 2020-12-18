# Function ki zaroorat hum tab padti hai jab hume ek hi Formula aa work ko apne program mei kabhi bhi call krna padh jaaye
# Ek hota hai Built in Function Like this:-
a = 9
b = 8
c = sum((a, b)) 


# Lekin Kabhi - Kabhi humko ese kaam krwane pad skte hai jo Predefined na ho to hum Function ko define krte ha


# Defining a fuction 
# Syntax :- def fuc1(variable agar chahiye to le lo):
                # Iss ident ka matlab ab hum fuctions ke andar ghus gye hai



# Example of a fuction 
def function1(a, b):
    """This fuction does the sum of two no."""
    print("Hello you are in function 1", a+b)
function1(2,3) # This statement means calling  a fuction aur jo bracket mei value hai wo A and B ki hai.


# Docstrings
# Jab humara program bohut bada ho jaata hai tab kabhi kabhi confusion ho skti hai ki iss fuction ka kaam kya hai... iss case mei doctring ka istamal kiya jaa skta hai jisse hum log fuction mei ek COMMENT likh skte hai 


# Writing a doctring
""" Your Message"""


# Calling a Docstring
print(function1.__doc__)


# Example of a fuction with a doctring
def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

v = function2(5, 7)
print(v)
print(function2.__doc__)
