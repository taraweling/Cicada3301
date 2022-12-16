import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, player, name, desc, weight):
        self.name = name
        self.desc = desc
        self.loc = None
        self.weight = weight
        self.player=player

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
        
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

    def use(self):
        print ("you cannot use the " + self.name)


"Perform the command of read on these items to increase your intelligence."
class Books(Item):
    def __init__(self, player, name,desc,weight):
        Item.__init__(self, player, name,desc,weight)
        self.readBefore = False

    def use(self):
        self.read()
        

    def read(self):
        if self.readBefore:
            clear()
            print("You have read this book already.")
        else:
            self.player.intelligence += 10
            self.player.readBefore = True
            clear()
            print("You have gained +10 intelligence")

    
"Increases health but decreases intelligence. "

class Spaghetti(Item):

    def __init__(self, player):
        self.name = "Spaghetti Code"
        self.desc = "Mmmm, tasty! Get plus 10 health but lose 1 intelligence...for unmaintainable code."
        self.loc = None
        self.weight = 1
        self.player=player

    
    def use(self):
        self.affect()
    
    def affect(self):
        self.player.intelligence -= 1
        if (self.player.health + 10) > self.player.healthmax:
            self.player.health += abs(self.player.maxhealth - self.player.health)
        else:
            self.player.health += 10
            
        self.player.items.remove(self)

        print("Congratulations! You slurp up the spaghetti code and hope you don't regret it. At least it isn't lasagna code?")
        time.sleep(0.5)
        print("Oh, and you lost one intelligence point for writing incomprehensible code...")
        time.sleep(0.25)
        input("Press enter to continue...")


"Decreases intelligence and health. Oof!"
class Crypto(Item):

    def __init__(self, player):
        self.name = "₿itcoin"
        self.desc = "(Not affiliated with blockchain technology)... The only crypto that Cicada 3301 supports is cryptographic one. Eating ₿ will  decrease your intelligence by 10 points (as a screw you). Also, be warned that this has a weight of 5 to account for your burdensome sins."
        self.loc = None
        self.weight = 5
        self.player=player
    
    def damage(self):
        if (self.player.health - 10) < 0:
            self.player.health -= abs(self.player.maxhealth - self.player.health)
        else:
            self.player.health -= 10
        
        if (self.player.intelligence - 5) < 0:
            self.player.intelligence -= abs(self.player.maxintelligence - self.player.intelligence)
        else:
            self.player.intelligence -= 5

            self.player.items.remove(self)
            print("Oops! You become about 10%% less intelligent")
            time.sleep(0.5)
            print("That's what you get for being a crypto bro...")
            time.sleep(0.25)
            print("You lost 5hp! Be careful next time!")
            time.sleep(0.25)
            input("Press enter to continue in shame...")


