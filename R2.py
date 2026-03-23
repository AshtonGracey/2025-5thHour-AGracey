#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
emplist = []
#3. Create a list that contains the names of everyone in the classroom.
People = ["Ashton", "Bryson","Hogan","Sam","Aiden","Brennlyn","Ivan","Dylan"]
#4. Print the list from #3, sort the list, then print the list again.
print(People)
People.sort()
print(People)
#5. Append 5 different integers into the empty list from #2 and print the list.
emplist.append(1)
emplist.append(3)
emplist.append(2)
emplist.append(4)
emplist.append(5)
print(emplist)
#6. Add together the middle three numbers in the list from #2 and print the result.
print(emplist[1]+emplist[2]+emplist[3])
#7. Remove the very first number in the list from #2. Print the new first number.
emplist.pop(0)
print(emplist[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
peopledict = {
    "name" : "Ashton",
    "grade" : "11th",
    "favorite color" : "purple",
}

#9. Using the update function, add a fourth key and value determining your favorite candy.
peopledict.update({"favorite candy" : "snickers"})
#10. Print ONLY the values of the dictionary from #8.
print(peopledict["name"])
print(peopledict["grade"])
print(peopledict["favorite color"])
print(peopledict["favorite candy"])