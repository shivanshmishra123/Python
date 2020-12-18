# Instructions:
# 1. You are free to use anything we've studied till now.
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.

chanceleft = 4
chancestaken = 5 - chanceleft
while(True):
    num = int(input("Guess the no. and enter it"))
    if num == 100:
        chanceleft = chanceleft - 1
        print("Yes!! You got it right and the no was 100")
        print("You took " + str(chancestaken) + " guess to complete the game")
        break
    elif chanceleft == 0:
        print("Game Over!! You exhausted your all chance")
        break
    else:
        print("Try Again\n")
        chanceleft = chanceleft - 1
        continue 