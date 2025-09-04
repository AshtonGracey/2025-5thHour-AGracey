#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
people = ["waylon", "mardi", "tucker", "angel", "stryker"]
print(people)
#2. Append a new name onto the Name List.
people.append(input("insert person to list"))
#3. Print out the 4th name on the list.
print(people[3])
#4. Create a list with 4 different integers in it.
numberlist = [1,2,5,9]
print(numberlist)
#5. Insert a new integer into the 2nd spot and print the new list.
numberlist.insert(2, 7)
print(numberlist)
#6. Sort the list from lowest to highest and print the sorted list.
numberlist.sort(reverse=True)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numberlist_subsum = numberlist[1] + numberlist[2] + numberlist[3]
print(numberlist_subsum)
#8. Create a list with two strings, two variables, and too boolean values.
otherlist = [ "ball","desk","variable" ,12,23 ,  True, True ]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(otherlist.append(input("insert here")))