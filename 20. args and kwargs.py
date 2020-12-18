# Dekho jab bhi hum koi fuction likhte hai aur phir usko likhne ke baad hume usme koi ek aur arguents pass 
# krwani ho to hume bohut mehnat krni padti hai jaise :--
# def name(a,b,c,d):
#     print(a , b , c , d)
# name("Shivansh","Harry","Rohan","SkillF")
# ab dekh lo iss fuction mei agar mujhe The Programmer ka bhi naam add krna hota to mujhe pehle 
# ek aur argument e lagani padta aur phir uske baad e ko bhi print krwana padta aur fuction ko call krte
# wakt bhi usse likhna padta.... To isse accha hota hai *args

# Example of *args

# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)
  

