# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

num1 = int(input("Enter the first no."))
num2 = int(input("Enter the second no."))
operator = input("Enter the mathematical operator you want to use")

if num1 == 45 and num2 == 3 and operator == "*":
    print("555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("77")
elif num1 == 56 and num2 == 6 and operator == "/":
    print("4")   

elif operator == '+':
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)