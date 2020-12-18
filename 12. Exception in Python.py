# Exception matlab jo error aa rha hai program ko run krne mei
# Aur issi exception ko print krne ke liye pehle hum except fuction ka use krke uss exeption ko le lete hai 

# Example
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try: # try ka matlab yahi hai ki pehle wo isko try krega .......Nothing special
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e: #iss line mei "as e" ka matlab hai ki humne exception ko E variable assign kr diya hai 
    print(e) # Aur phir humne iss line mei uss exception ko print kr diya 




