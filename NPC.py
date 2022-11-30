import random 
import updater
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# NPCs are ...
class NPC:
    def __init__(self, name, desc, room):

        self.name = name
        self.description = desc
        self.room = room

        #self.possibleconversations = []
        #self.currentConversation = None
        #self.convoitshouldbenum = 0
        #self.possiblerooms = [room]

        room.addCharacter(self)
        updater.register(self)

    def update(self):
        pass

    def convo(self, prompt, ans1, ans2, ans3, ans4):
        # convo
        # how many options
        pass



    def describe(self):
        clear()
        print()
        print(self.desc)
        print()
        input("Press...")

    def moveTo(self, room):
        self.room.removeCharacter(self)
        self.room = room
        room.addCharacter(self)

"""
# The mysterious persona Cicada 3301
## This class can do cool things
like....



class Cicada(NPC):
    def __init__(self, player, desc):
        self.name = "3301"
        self.



"""