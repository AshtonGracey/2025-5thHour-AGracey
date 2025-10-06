#Name: Ashton Gracey
#Class: 6th Hour
#Assignment: HW9

import random
#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
randomvariable1 = random.randint(0,100)
randomvariable2 = random.randint(0,100)
randomvariable3 = random.randint(0,100)
randomlist = [randomvariable1,randomvariable2,randomvariable3]
#3. Print the list.
print(randomlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if randomvariable1 >= randomvariable2 and randomvariable1 >= randomvariable3:
        print("randomvariable1 is the greater")
elif randomvariable2 >= randomvariable1 and randomvariable2 >= randomvariable3:
        print("randomvariable2 is the greater")
elif randomvariable3 >= randomvariable1 and randomvariable3 >= randomvariable2:
        print("randomvariable3 is greater")
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(randomlist)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num %2 == 0:
    print("num is divisible by 2")
elif num %3 == 0:
    print("num is divisible by 3")
elif num %2 == 0 and num %3 == 0:
    print("num is divisible by both")
else: print("num is not divisible by either")

