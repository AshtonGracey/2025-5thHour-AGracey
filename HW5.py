
#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
people = [2, 3, 5, 6, 7, 8 , 1 , 4, 9]
#2. Sort the list from highest to lowest.
people.sort(reverse=True)
print(people)
#3. Create an empty list.
ashton = []
#4. Remove the median number from the first list and add it to the second list.
numberfive= people[4]
people.pop(4)
ashton.append(numberfive)
#5. Remove the first number from the first list and add it to the second list.
numberone = people[0]
people.pop(0)
ashton.append(numberone)
#6. Print both lists.
print(ashton)
print(people)
#7. Add the two numbers in the second list together and print the result.
numbersum = sum(ashton)
print(numbersum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
ashton.pop(1)
ashton.pop(0)
people.append(numberfive)
people.append(numberone)
#9. Sort the first list from lowest to highest and print it.
people.sort()
print(people)