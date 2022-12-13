import os
import random
from item import Item
import monster

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.items = []
        self.intelligence = 50
        self.maxIntelligence = 100
        self.energy = 100
        self.unlocked=[] #list of barriers that player has passed already
        self.level = 1
        # add traits
        self.alive = True
        self.itemWeights = 0 # make inventory have a limit
    
    # list of actions: levelUp, goDirection, pickup, drop, getItemName, showInventory, showStatus, removeItem, attackMonster

    def levelUp(self):
        self.level += 1
    
    def goDirection(self, direction):

        if self.location.getDestination(direction) == None:
            print("ERROR 404")
            input("Press enter to go back...")
            return
            
        if self.location.barrier != [] and self.location.getDestination(direction).barrier != []:
            if self.location.barrier[0].type == "Barrier" and self.location.barrier[0].open:
                self.location = self.location.barrier
                if self.location not in self.unlocked:
                    print ("Congratulations on completing this level. You are one step closer to discovering Cicada's secret")
                    self.level+=1
                    self.unlocked.append(self.location)
                
                print ("You have entered "+ str(self.location.desc+ "."))
               
            else:
                print("Forbidden")
                input("Press enter to go back...")
            return

        #temporarily always does this
        self.location = self.location.getDestination(direction)


    def pickup(self, item):
        self.itemWeights += item.weight
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

    def drop(self, item):
        self.itemsweight -= item.weight
        self.removeItem(item)
        item.loc = self.location
        self.location.items.append(item)

    def getItemName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i 
        return False

    #def flyTo()
    # you go to another room

    def showInventory(self):
        clear()
        if len(self.items) == 0:
            print()
            print("You have nothing.")
        else:
            print("Your inventory currently consists of:")
            print()
            for i in self.items:
                print(i.name)
            print()
            input("Press enter to continue...")

    def showStatus(self):
        clear()
        print("Your current status:\n")
        print(str(self.name))
        #+ ", Level: " + str(self.level))
        print("Intelligence:\t" + str(self.intelligence) + "/" + str(self.maxIntelligence))
        print()
        if self.intelligence <= 10:
            print("Cicada only wants to best and brightest. You can only level up ")
        else:
            print("We'll see if you have what it takes...")
        input("Press enter to continue...")

    def removeItem(self, item):
        self.items.remove(item)

    #def getItemName(self, requesteditem):
    #    for i in self.items:
    #        if i.name.lower() == requesteditem:
    #            return i

    # how does attacking monsters work?
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")


        # you can define some other functions about monster attacking etc, espcially one that allows you to make choices in fights

        """
            def examineItem(self,item?)
            
            def useItem(self,)
        """


# create a class for powers or magic and such?