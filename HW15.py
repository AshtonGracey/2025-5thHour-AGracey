#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library.
import random
import math

from HW3 import integerVar1

#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("enter an integer"))
b = int(input("enter an integer"))
c = int(input("enter an integer"))
#4. Add a and b together, then divide the sum by c. Print the result.
sum = a + b
print(sum)
p = sum / c
print(p)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
p = round(p)
print(p)
if p % 2 == 0 :
    print("the number is even")
else:
    print("the number is odd")
#6. Create a list of five different random integers between 1 and 10.
int1 = random.randint(1, 10)
int2 = random.randint(1, 10)
int3 = random.randint(1, 10)
int4 = random.randint(1, 10)
int5 = random.randint(1, 10)
randomlist = [int1, int2, int3, int4, int5]
print(randomlist)
#7. Print the 4th number in the list.
print(randomlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
rnd = random.randint(1, 10)
randomlist.append(rnd)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randomlist.sort(reverse= False)
print(randomlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i < 100:
    i+= i
    print(i)
#11. Create a list containing the names of five other students in the classroom.
studentlist = ["Dylan" , "Ivan" "Sam","Hogan","Jude"]
#12. Create a for loop that individually prints out the names of each student in the list.
for person in studentlist:
    print(person)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
e = 1
for e in range(1 , 101):
    print(e)
    if e % 10 == 0:
        break
#14. Free space. Do something creative. :)
slotmachine = ["cherry" , "lemon" , "7" , " bar"]
print(random.choice(slotmachine))
random.shuffle(slotmachine)
print(random.choice(slotmachine))
random.shuffle(slotmachine)
print(random.choice(slotmachine))
random.shuffle(slotmachine)