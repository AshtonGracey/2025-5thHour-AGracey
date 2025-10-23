#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: HW10

#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = False
Admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminlogin = 2
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if Admin == True:
            print("Welcome")
            adminlogin += 1
        else:
            print("You dont have permission")
    else:
        print ("Your login is false")
else:
    print("You dont have wifi")
