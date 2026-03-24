#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print("Hello World!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
mouse = random.randint(1,10)
keyboard = random.randint(1,10)
desk = random.randint(1,10)
print(mouse, keyboard, desk)
#3. Create a list containing 5 strings listing 5 colors.
colorlist = ["red", "blue", "green", "yellow", "purple"]

#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(colorlist))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if mouse == keyboard == desk:
    print("they are all equal")
elif mouse < keyboard and mouse < desk:
    print("mouse is the smallest")
elif keyboard < mouse and keyboard < desk:
    print("keyboard is the smallest")
elif desk < keyboard and desk < mouse:
    print("desk is the smallest")
elif mouse == keyboard and mouse < desk:
    print("mouse and keyboard are the smallest")
elif mouse == desk and mouse < keyboard:
    print("mouse and desk are the smallest")
else:
    print("desk and keyboard are the smallest")

