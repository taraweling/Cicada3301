import os

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


"""
All items I want to add should inherit from the item class

Something that can heal


Something that can



"""
