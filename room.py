import random

class Room:
    def __init__(self, location, description):
        self.desc = description
        self.location = location
        self.monsters = []
        self.exits = []
        self.items = []
        self.containers = []
        self.characters = []
        self.barriers = []
        self.exits = []

    # Exits
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def removeExit(self, exitName, destination):
        self.exits.remove([exitName, destination])
    def exitNames(self):
        return [x[0] for x in self.exits]

    # Destination
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
        return None

    # Connections
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    # removes connections to other rooms
    def removeConnections(room1, dir1, room2, dir2):
        room1.removeExit(dir1, room2)
        room2.removeExit(dir2, room1)
        pass
    # one-way connects rooms - cannot leave
    def semiConnectRooms(room1, dir2, room2):
        room1.addExit(dir2, room2)
    

    # Items
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    # Containers
    def addContainer(self, container):
        self.containers.append(container)
    def removeContainer(self, container):
        self.containers.remove(container)
    def hasContainers(self):
        return self.containers != []
    def getContainerByName(self, name):
        for i in self.containers:
            if i.name.lower() == name.lower():
                return i
        return False

    # Monsters
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False

    # Characters
    def addCharacter(self, npc):
        self.characters.append(npc)
    def removeCharacter(self, npc):
        self.characters.remove(npc)
    def hasCharacters(self):
        return self.characters != []
    def getCharacterByName(self, name):
        for i in self.characters:
            if i.name.lower() == name.lower():
                return i
        return False

    # Barriers
    def hasBarriers(self):
        return self.barriers != []
    def getBarrierByName(self, name):
        for i in self.barriers:
            if i.name.lower() == name.lower():
                return i
        return False

    def randomNeighbor(self):
        return random.choice(self.exits)[1]
    
    def update(self):
        pass

class Puzzle(Room):
    def __init__ (self, description):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.containers = []
        self.characters = []
        self.barrier = []
        self.exits = []
        self.solved=False
 

#Class for Barrier preventing entry into other rooms before puzzle has been correctly answered 

class Barrier(Room):
    def __init__(self, name, desc, origin, dir): #name is inputted, as well as the room the player is coming from (so that the player can go back even if barrier is closed)
        Room.__init__(self,desc)
        self.name=name
        self.open=False
        self.closed=self.exits
        self.origin=origin
        self.dir=dir

    def closeBarrier(self):
        self.open=False
        self.exits=[]
        self.addExit(self.dir, self.origin)       

    def openBarrier(self):
        self.removeExit(self.origin, self.dir)
        self.open=True
        self.exits=self.closed
