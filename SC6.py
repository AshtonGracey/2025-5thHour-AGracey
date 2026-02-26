#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)
class Character:
    def __init__(self, hp, init,ac,attackmod, damage):
        self.hp = hp
        self.init = init
        self.ac = ac
        self.attackmod = attackmod
        self.damage = damage
LaeZel = Character(48, 1, 17, 6, random.randint(1,6) + random.randint(1,6) + 3)
shadowheart = Character(40, 1, 18, 4, random.randint(1,6) + 3)
gale = Character(32 ,1, 14 , 6, random.randint(1,10) + random.randint(1,10))
Astarion = Character(40, 3, 14, 5, random.randint(1,8) + random.randint(1,6) + 4)
goblin = Character(7, 0, 12, 4,random.randint(1,6) + 2)
orc = Character(15, 1, 13, 5, random.randint(1,12) + 3)
troll = Character(84, 1, 15, 7, random.randint(1,6) + random.randint(1,6) + 4)
mindflayer = Character(71, 1, 15, 7,  random.randint(1,10) + random.randint(1,10) + 4)
dragon = Character(127, 2, 18, 7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)
player1 = random.randint(1,20)
player2 = random.randint(1,20)
if player1 > player2:
    print("hero goes first")
    player1first = True
else :
    print("hero goes second")
    player1first = False
while gale.hp >0 and goblin.hp > 0:
    if player1first == True:
        print("Gale goes first")
        player1attack = random.randint(1,20)
        print(player1attack)
        if player1attack == 20 :
            goblin.hp -= gale.damage *2
            print(f"Gale hits Goblin  for {gale.damage} *2)")
        elif player1attack == 1:
            print("roll natural 1, Miss")
        elif player1attack + gale.attackmod >=goblin.ac:
            goblin.hp -= gale.damage
            print(f"Gale hits Goblin for{gale.damage} damage")
        else:
            print("Gale Missed Attack")
        player2attack = random.randint(1,20)
        print(player2attack)
        if player2attack == 20 :
            gale.hp -= goblin.damage * 2
            print(f"Goblin hits Gale for{goblin.damage * 2}")
        elif player2attack ==1:
            print("roll natural 1, Miss")
        elif player2attack +goblin.attackmod >= gale.ac:
            gale.hp -=goblin.damage
            print(f"Goblin hits Gale for{goblin.damage} damage")
        else:
            print("Goblin Missed Attack")
    else:
        print("Goblin goes first")
        player2attack = random.randint(1,20)
        print(player2attack)
        if player2attack == 20 :
            gale.hp -= goblin.damage * 2
            print(f"Goblin hits Gale for{(goblin.damage * 2)}")
        elif player2attack ==1:
            print("roll natural 1, Miss")
        elif player2attack +goblin.attackmod >= gale.ac:
            gale.hp -= goblin.damage
            print(f"Goblin hits Gale for{goblin.damage} damage")
        else:
            print("Goblin Missed Attack")
            player1attack = random.randint(1, 20)
            print(player1attack)
        if player1attack == 20:
            goblin.hp -= gale.damage * 2
            print(f"Gale hits Goblin for{gale.damage * 2}")
        elif player1attack == 1:
            print("roll natural 1, Miss")
        elif player1attack + gale.attackmod >= goblin.ac:
            goblin.hp -= gale.damage
            print(f"Gale hits Goblin for{gale.damage}damage")
        else:
            print("Gale Missed Attack")