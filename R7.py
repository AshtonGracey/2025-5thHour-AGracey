#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that in its self and the three attributes: name, grade, color.
class Ae:
    def __init__(self,name, grade, color):
        self.name = name
        self.grade = grade
        self.color = color
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.
    def grade1(self):
        if self.grade < 12:
            self.grade +=1
        else:
            self.grade ="you have graduated"
#3. Make a def function within the class that offers the user to input/change their favorite color.
    def color1(self):
        self.color = input("enter your favorite color")

