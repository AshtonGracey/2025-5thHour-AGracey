#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that prints out "Hello World!"
def Hello_world():
    print("Hello World")
Hello_world()
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def average(num1, num2, num3):
    answer = (num1 + num2 + num3) / 3
    print(answer)
average(10,12,2)


#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animals):
    print("the 3rd animal is", animals[2])
animal_list("cat", "dog", "bird", "rabbit", "bat")

#4. Create a def function that loops from 1 to the number put in the argument.
def loop(num):
    for i in range(1, num + 1):
        print(i)
loop(5)
#5. Call all of the functions created in 1 - 4 with relevant arguments.

#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def asd():
    global x
    x =x*random.randint(1,5)
    print(x)
asd()
#8. Print the new value of x.
print(x)
