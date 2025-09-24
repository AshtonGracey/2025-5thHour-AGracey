#Name:
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
classdict = {
    "class" : [ 10, 11, 12 ],
    "grade" : "12",
    "student" : "name"
}
#3. Print the keys of the dictionary from #2.
print(classdict.keys())
#4. Print the values of the dictionary from #2
print(classdict.values())
#5. Print one of the three numbers from the list by itself
print(classdict["class"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
classdict.update( {"last name" : "Jones"} )
#7. Print the entire dictionary from #2 with the updated key and value.
print(classdict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
studentdict = {
    "student1" : {
         "name" : "waylon" ,
        "class" : "11" ,
         "height" : "5'10"
    },
    "student2" : {
         "name" : "Mardi" ,
         "class" : "12" ,
         "height" : "5'3"
    },
    "student3" : {
     "name" : "sam" ,
    "class" : "11" ,
    "height" : "5'9"
    },
}
#9. Print the names of all three classmates on the same line.
print(studentdict["student1"]["name"] , studentdict["student2"]["name"] , studentdict["student3"]["name"] )
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
studentdict.pop("student1")
print(studentdict)