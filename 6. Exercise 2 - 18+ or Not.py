# You have to check whether the user is 18+ or not and tell him whether he can drive or not
age =  int(input("Enter your age"))

if age == 18:
    print("You are eligible only if you have good driving skills")
if age > 18:
    print("You are eligible to drive")
if age < 18:
    print("You are not eligible to drive")