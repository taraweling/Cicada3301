import random
import updater
import os 

# our monsters are essentially puzzles
class Monster:
    def __init__(self, name, room): # points of monster and other input traints
        self.name = name


        self.health = health

        
        self.room = room
        # self.whatever = whatever
        

        room.addMonster(self)
        updater.register(self)

    def update(self):
        #if random.random() < .5: # what does this mean?
        #    self.moveTo(self.room.randomNeighbor())
        pass

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)

    def die(self):
        self.room.removeMonster(self)
        self.room.update() # why did I add this again?
        updater.deregister(self)


"""
How many monster subclasses do I want?
Law enforcement should be one subclass
News/Media should be another
Who are the enemies?
What are the traits they inherit from the monster class?
Cryptography
- We could personify different cyphers and have the person fight them
Collaborators -> 
"""