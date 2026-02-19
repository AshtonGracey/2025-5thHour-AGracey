#Name: Ashton Gracey
#Class: 5th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store:
    def __init__(self ,stock,cost,weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_cost(self):
        self.cost = self.cost * 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
item1 = store(34 , 53 , 34)
item2 = store(65 , 23 , 38)
item3 = store(999, 28 , 45)
#3. Print the stock of all three objects and the cost of the second store item.
print(item1.stock)
print(item2.stock)
print(item3.stock)
print(item2.cost)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
item2.double_cost()
print(item2.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
item3.stock = item3.stock /4
print(round(item3.stock))

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del item1
try :
    print(item1.weight)
except :
    print("Item out of stock")

