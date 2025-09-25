#Name:Ashton Gracey
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
enemiesdict = {
    "enemy1" : {
        "name" : "waylon" ,
        "damage": 20 ,
        "health" : 100,
    },
    "enemy2" : {
         "name": "mardi" ,
        "damage" : 1 ,
        "health" : 1,
    },
    "enemy3": {
        "name": "sam",
        "damage": 40,
        "health": 120,
    },
    "enemy4": {
        "name": "ivan",
        "damage": 30,
         "health": 20,
    },
    "enemy5": {
         "name": "coach_mack",
        "damage": 60,
        "health": 140,
    },
}
enemiesdict["enemy1"]["damage"] =int(input("Enemy1Damage"))
print(enemiesdict["enemy1"])
enemiesdict["enemy2"]["damage"] =int(input("Enemy2Damage"))
print(enemiesdict["enemy2"])
enemiesdict["enemy3"]["damage"] =int(input("Enemy3Damage"))
print(enemiesdict["enemy3"])
enemiesdict["enemy4"]["damage"] =int(input("Enemy4Damage"))
print(enemiesdict["enemy4"])
enemiesdict["enemy5"]["damage"] =int(input("Enemy5Damage"))
print(enemiesdict["enemy5"])