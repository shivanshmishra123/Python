import random 
output = ["Snake","Water","Gun"]
chance = 10
computerwon = 0
playerwon = 0
Draw = 0
while(True):
    if chance == 0:
        print("\nGame over")
        print("And the results were as follows:-")
        print("")
        print(f"No of times Computer won = {computerwon}")
        print(f"No of times you won = {playerwon}")
        print(f"No of times draw = {Draw}")
        break
    
    rand = random.choice(output)
    choice = int(input("\nPress 1 for Snake, 2 for Water and 3 for Gun\n"))

    if choice ==  1 and str(rand) == output[0]:
        print("Draw")
        Draw = Draw + 1
    elif choice ==  2 and str(rand) == output[1]:
        print("Draw")
        Draw = Draw + 1
    elif choice ==  3 and str(rand) == output[2]:
        print("Draw")
        Draw = Draw + 1


    if choice ==  1 and rand == output[1]:
        print("You won")
        playerwon = playerwon + 1
    elif choice ==  1 and rand == output[2]:
        print("You lost")
        computerwon = computerwon + 1


    if choice ==  2 and rand == output[0]:
        print("You lost")
        computerwon = computerwon + 1
    elif choice ==  2 and rand == output[2]:
        print("You won")
        playerwon = playerwon + 1


    if choice == 3 and rand == output[0]:
        print("You won")
        playerwon = playerwon + 1
    if choice == 3 and rand == output[1]:
        print("You lost")
        computerwon = computerwon + 1
        
    chance = chance - 1    