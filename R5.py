#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW-R5

#1. Create a list of the names of all the students in the classroom.
People = ["Ashton", "Bryson","Hogan","Sam","Aiden","Brennlyn","Ivan","Dylan"]
#2. Create a for loop that prints the names of every student in the list.
for person in People:
    print(person)
#3. Using the "in" operator (hint: Google), create a for loop that only prints
#the name of a student if the letter "e" is in it.
print("-----")
for person in People:
    if "e" in person:
        print(person)