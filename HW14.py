#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW14


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for b in range(5,0,-1):
    print(b)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for w in range(1 ,31,+1):
    if w % 2 == 0:
        print(w)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for x in range(1,31,+1):
    if x % 3 == 0:
        continue
    else:
        print(x)
#4. Create a for loop that prints 5 different animals from a list.
animalList = ["Jaguar", "Cheetah", "Lion", "Cougar", "Tiger"]
for animal in animalList:
    print(animal)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
t = (input("Enter a word: "))
r = ''
for waylon in t:
    r = waylon + r
print(r)
#6. Create a list containing 10 integers of your choice and print the list.
numlist  = [1,2,3,4,5,6,7,8,9,10]
print(numlist)
#7. Create two empty variables named evenNumbers and oddNumbers.
evennumbers = []
oddnumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for number in numlist:
    if number % 2 == 0:
        evennumbers.append(number)
    else: oddnumbers.append(number)
    continue
print(evennumbers)
print(oddnumbers)
#9. Create a variable that asks the user for an integer and an empty integer variable.
y = int(input("Enter a number: "))
g = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for l in range(1,y+1):
    g*=l
print(y)