# These are the statements which are used to Break/End/Terminate a while loop program in the middle
# or to instruct the computer to continue the while loop program
while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
