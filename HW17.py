#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps():
    playerrps = int(input("enter 1 for rock, 2 for paper, 3 for scissors: "))
    x = random.randint(1,3)
    print(x)
    if x == playerrps:
        print("You tie")
    elif x == 1 and playerrps == 2:
        print("You win")
    elif x == 1 and playerrps == 3:
        print("You lose")
    elif x == 2 and playerrps == 1:
        print("You lose")
    elif x == 2 and playerrps == 3:
        print("You win")
    elif x == 3 and playerrps == 1:
        print("You win")
    elif x == 3 and playerrps == 2:
        print("You lose")
    else:
        print("Invalid input")
    repeat()


#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def repeat():
    replayinput = input("Would you like to play again? (y/n) ")
    if replayinput == "y" or "Y":
        rps()
    else:
        print("Thank you for playing")
rps()