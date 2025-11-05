#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: HW12

import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print("Hello world")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j =1
while j <= 30:
    j+=1
    if j % 2 == 0:
        print(j)

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3
p = 0
while p <= 30:
    p+=1
    if p % 3 == 1:
        print(p)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
r = random.randint(1,6)
while r == 6:
    if r ==1:
        continue
    print(r)
    break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
w= int(input("enter a number"))
while w>=1:
    w = (int(input("enter a number")))
