#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def Hello():
    print("Hello World")
#2. Create two empty integer variables named "heads" and "tails"
heads =0
tails =0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin():
    global heads,tails
    for i in range(1,101):
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            heads+=1
        else:
            tails+=1

#4. Call the "Hello world" and "Coin Flip" functions here
Hello()
coin()
#5. Print the final result of heads and tails here
print("Heads =",heads,"Tails =",tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag =["red", "blue", "yellow", "green", "pink"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    r = (random.choice(beanbag))
    print(r)
    beanbag.remove(r)
    repeat()
print(beanbag)

print(beanbag)
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat():
    replay_input =  input("would you like to pull another bean Y/N?")
    if replay_input == "Y" or replay_input == "y":
        bean()
        print(beanbag)
    else:
        print("Thanks for playing!")


#9. Call the "Bean Pull" function here
bean()
