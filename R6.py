#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: HW-R6


#1. Create a def function that prints out "Hello World!". Call the function.
def world():
    print("Hello World!")
world()
#2. Create a def function that prints your name. Call the function with the name as the argument.
def name(name):
    print(name)
name("ashton")

#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.
def list1(*list):
    avg = sum(list) / len(list)
    print(avg)
list1(1,2,3,4,5)
#4. Call the function from #3 but with a new list of different numbers.
list1(9,2,54,4,20)
#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, make z equal the sum of x and y, make x equal y, then y equal z.
def numbers(x , y):
    for num in range(10):
        z = x +y
        x = y
        y = z
        print(x)
#6. Call the function from #5 with the arguments for x and y being 0 and 1.
numbers(0 , 1)