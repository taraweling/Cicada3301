import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, weight):
        self.name = name
        self.desc = desc
        self.loc = None
        self.weight = weight

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
        
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
    

"Perform the command of read on these items to increase your intelligence."
class Books(Item):
    def __init__(self, name, desc, weight,player):
        Item.__init__(self,name,desc,weight)
        self.user = player
        self.readBefore = False
        

    def read(self):
        if self.readBefore:
            clear()
            print("You have read this book already.")
        else:
            self.intelligence += 10
            self.readBefore = True
            clear()
            print("You have gained +10 intelligence")

    
"Increases health but decreases intelligence. "

class Spaghetti(Item):

    def __init__(self):
        self.name = "Spaghetti Code"
        self.desc = "Mmmm, tasty! Get plus 10 health but lose 1 intelligence...for unmaintainable code."
        self.loc = None
        self.weight = 1
    
    def affect(self, player):
        player.intelligence -= 1
        if (player.health + 10) > player.healthmax:
            player.health += abs(player.maxhealth - player.health)
        else:
            player.health += 10
            
        player.items.remove(self)

        print("Congratulations! You slurp up the spaghetti code and hope you don't regret it. At least it isn't lasagna code?")
        time.sleep(0.5)
        print("Oh, and you lost one intelligence point for writing incomprehensible code...")
        time.sleep(0.25)
        input("Press enter to continue...")


"Decreases intelligence and health. Oof!"
class Crypto(Item):

    def __init__(self):
        self.name = "₿itcoin"
        self.desc = "(Not affiliated with blockchain technology)... The only crypto that Cicada 3301 supports is cryptographic one. Eating ₿ will  decrease your intelligence by 10 points (as a screw you). Also, be warned that this has a weight of 5 to account for your burdensome sins."
        self.loc = None
        self.weight = 5
    
    def damage(self, player):
        if (player.health - 10) < 0:
            player.health -= abs(player.maxhealth - player.health)
        else:
            player.health -= 10
        
        if (player.intelligence - 5) < 0:
            player.intelligence -= abs(player.maxintelligence - player.intelligence)
        else:
            player.intelligence -= 5

            player.items.remove(self)
            print("Oops! You become about 10%% less intelligent")
            time.sleep(0.5)
            print("That's what you get for being a crypto bro...")
            time.sleep(0.25)
            print("Oh, and you lost 5 hp. Just because.")
            time.sleep(0.25)
            input("Press enter to continue in shame...")


