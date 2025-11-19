#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
numofplayers = int(input("# of players: "))
ratingslist = []
for number in range(numofplayers):
    rating = int(input("Enter a rating 1-5"))
    while rating >5 or rating < 1:
        print("Your rating has to be 1-5 ")
        break
    else: ratingslist.append(rating)
averagerating = sum(ratingslist)/len(ratingslist)
print("The average rating is: ", averagerating)

