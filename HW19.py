#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import animal_list, Hello_world , average , loop

#2. Call the functions here and run HW19
animal_list("cat", "dog", "bird", "rabbit", "bat")
Hello_world()
average(10,12,2)
loop(5)
#3. Delete all calls from HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try :
    print(x)
except :
    print("hello world")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Value Error. Needs to be an integer")
except:
    print("Unknown error.")

#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    k = int(input("give me an integer"))
    print(k)
except:
    raise ValueError("it needs to be an integer")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i = 5
while i > 0:
    print(i)
    i -=1
if i <= 0:
     raise ValueError("below zero")
