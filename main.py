from room import Room # can add other classes
#from room import Barrier, quizBarrier
from player import Player
from item import Item # other item classes as well
from monster import Monster
from NPC import NPC #, Cicada
import os
import updater
import time
import sys



""" creating the world """

def createWorld():

    ### 

    # creating rooms (aka cities) - and subrooms (aka puzzles) #

    # home city = pdx
    pdx = Room("Portland, OR: where you live. More description of clues in the city... ")
    p1 = Room("Puzzle 1: ")
    p2 = Room("Puzzle 2: ")
    p3 = Room("Puzzle 3") 
    
    ### 
    
    # seoul, south korea 
    sol = Room("You are in Seoul...")
    s1 = Room("Puzzle 4")
    s2 = Room("Puzzle 5")
    s3 = Room("Puzzle 6")

    ###

    # erskineville, australia
    ekv = Room("You are in Erskineville...")
    e1 = Room("Puzzle 7")
    e2 = Room("Puzzle 8")
    ###

    # warsaw, poland
    war = Room("You are in Warsaw...")

    ###

    # haleiwa, hawaii
    hal = Room("You are in Haleiwa...")

    #connects all cities to each other
    cities=[sol, ekv, war, hal]
    for i in cities:
        for k in cities:
            if len(k.exits)==0:
                Room.connectRoom(i, "x", k, "y")
    
    # connecting rooms #
    
    ## portland 
    ### connections to other cities 
    Room.connectRooms(pdx, "x", sol, "y")
    Room.connectRooms(pdx, "x", ekv, "y")
    Room.connectRooms(pdx, "x", war, "y")
    Room.connectRooms(pdx, "x", hal, "y")

    ### connections to puzzles within the city
    Room.connectRooms()


    ## seoul 
    # Room.connectRooms(p1, " ", p2, " ")
    Room.connectRooms(r3, "east", r4, "west")
    Room.connectRooms(pdx, "north", r3, "south")
    Room.connectRooms(r2, "north", r4, "south")

    ###

    # creating items #
    i = Item("Rock", "This is just a rock.")
    i.putInRoom(r2)

    
    #Player.location = pdx

    # creating monsters #
    Monster("Bob the monster", 20, r2)

    ###

    # creating NPCs #
    #
    #
    #
    #
    #

###

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    time.sleep(0.2)
    print("Your intelligence: " + str(player.intelligence))
    print()
    print("Your location: " + str(player.location))
    print()
    print("Your level: " + str(player.level))

    # monsters / puzzles !
    #if player.location.hasMonsters():
    #    print("This room contains the following puzzle(s)")
    #    for m in player.location.monsters:
    #        time.sleep(0.5)
    #        print(m.name)
    #    print()
    #else:
    #    pass
    
    # items
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            time.sleep(0.5)
            print(i.name)
        print()
    
    # characters
    if player.location.hasCharacters():
        print("This room contains the following characters:")
        for i in player.location.characters:
            time.sleep(0.5)
            print(i.name)
        print()

    # barriers
    if player.location.hasBarriers():
        print("This room contains the following obstacles:")
        for i in player.location.barriers:
            time.sleep(0.5)
            print(i.name)
        print()
    
    #
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()
    # anything extra

# help screen (make this cool and meta and stuff)
def showHelp():
    clear()
    print("help -- brings up this help screen")
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory") # make inventory cool, 
    print()
    print()
    print()
    print()
    print()
    # decipher thing
    print("pickup <item> -- picks up the item")
    print()
    input("Press enter to continue...")

"""

# scenes for different rooms
def c

# possible endings
def endings():
    clear()

    if...

"""


# GAME STARTS HERE

createWorld()


### intro scene ###
# add music
# print cicada intro

# Some cool ASCII printing functions
def eye():
    print(".           ..         .           .       .           .           .")
    time.sleep(0.2)
    print("      .         .            .          .       .")
    time.sleep(0.2)
    print("            .         ..xxxxxxxxxx....               .       .             .")
    time.sleep(0.2)
    print("    .             MWMWMWWMWMWMWMWMWMWMWMWMW                       .")
    time.sleep(0.2)
    print("              &&&*CICADA*IS*WATCHING*WMWMWMWM&&**:        .           .")
    time.sleep(0.2)
    print(" .      IIYVVXMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWxx...         .           .")
    time.sleep(0.2)
    print("     IWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMx..")
    time.sleep(0.2)
    print("   IIWMWMWMWMWMWMWMWMWMWCICADA***3301MWMWMWMWMWMWMWMWMWMWMWMWMx..        .")
    time.sleep(0.2)
    print("    ^^MWMWMWMWMWM^^^^^^^^.  .:..   .^^^^^MWMWMWMWMWMWMWMWMWMWMWMWMWti.")
    time.sleep(0.2)
    print(" .     ^^   . `  .: . :. : .  . :.  .  . . .  ^^^^MWMWMWMWMWMWMWMWMWMWMWMWMti=")
    time.sleep(0.2)
    print("        . .   :` . :   .  .*.* *....xxxxx...,*. *   * .^^^YWMWMWMWMWMWMWMWMWMW+")
    time.sleep(0.2)
    print("     ; . ` .  . : . .^ :  . ..XXXXXXXXXXXXXXXXXXXXx.    `     . ^YWMWMWMWMWMWMW")
    time.sleep(0.2)
    print(".    .  .  .    . .   .  ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  .     .     *******")
    time.sleep(0.2)
    print("        * :  : . : .  ..XXXXXWWW^   W88N88@888888WWWWWXX.   .   .        . .")
    time.sleep(0.2)
    print("   . ^ .    . :   ...XXXXXXWWW*    M88N88GGGGGG888^8M *WMBX.          .   ..  :")
    time.sleep(0.2)
    print("         :     ..XXXXXXXXWWW*     M88888WWRWWWMW8oo88M   WWMX.     .    :    .")
    time.sleep(0.2)
    print("           *XXXXXXXXXXXXWW*       WN8888WWWWW  W8@@@8M    BMBRX.         .  : :")
    time.sleep(0.2)
    print("  .       XXXXXXXX=MMWW*:  .      W8N888WWWWWWWW88888W      XRBRXX.  .       .")
    time.sleep(0.2)
    print("       ; . ` .  . : . .' :  . ..  x"+formatName(playername, 17)+"x.    `     . *YWMWMWMWMWMWMW")
    time.sleep(0.2)
    print("         **...^^^  MMM::.:.  .      W888N89999888O8W      . . ::::*RXV    .  : *")
    time.sleep(0.2)
    print(" .       ..'''''      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx")
    time.sleep(0.2)
    print("      ..' .            **MMmm .  .       WWWWWWW   . :. :,miMM***  : **`    .")
    time.sleep(0.2)
    print("   .                .       **MMMMmm . .  .  .   ._,mMMMM***  :  ^ .  :")
    time.sleep(0.2)
    print("               .                  **MMMMMMMMMMMMM*** .  : . ^   .        .")
    time.sleep(0.2)
    print("          .              .     .    .                      .         .")
    time.sleep(0.2)
    print(".                                         .          .         .")
    time.sleep(0.2)
    
def cicada():
    print("\n")
    print("      .:^~7!!7!!77!77?7!^:..                 !.:~?J!:.                   .:^^~!!~!~!!!!!7!~^:.      ")
    time.sleep(0.15)
    print("  .7J7!7J5:...?J77!^::^^JPY5YY5J!^.         ?&&YJ?!YP##~        .:^~7?J5GJ!7!~^^^?777.~#J^.75GBY.   ")
    time.sleep(0.15)
    print(" :@P :^^?~.. .B! ..:~~~~?Y^!YJPGB#BBG5?^.   !@P ~~ .J^^    .~7JYYJJ77??^ .~~!~J!~!.   .B7.:?J!?!.   ")
    time.sleep(0.15)
    print(" .J~!Y!7J!~77. !G7.:^!!!77~~Y?PG?!Y5P&&&BG5!5@&JBJ~PP.~JYGBBYYJ?7Y~~??~~!?!!~7P5::~  :PBJ5PYB5:     ")
    time.sleep(0.15)
    print("     .^7!75!~?J!5. .^JY7^.^^??????JJJ???..PG#G~.^.  ~?GY7~::?77Y5PJY?5Y7J7!J5?:^:  !5#PJJ5?.     ")
    time.sleep(0.15)
    print("        .~?7P?~JJ7.~##.~7?5G??7!~.. ..   ^5G5. ?@^.Y@^  :^^:^:.~7~!7?J5PJ55BY^^.~PJBYJJ7.           ")
    time.sleep(0.15)
    print("        .~?7P?~JJ7.~##.~7?5G??7!~.. ..   ^5G5. ?@^.Y@^  :^^:^:.~7~!7?J5PJ55BY^^.~PJBYJJ7.           ")
    time.sleep(0.15)
    print("           .!?PY^!BY^..::J&~!!:.          ^@@J^57.75!...    .      .YB&#:!7^..7JPPY~!:              ")
    time.sleep(0.15)
    print("               .:::  .7Y??7~Y5:           .&@:..^.^^.  .            ^@&~^Y55P~..                    ")
    time.sleep(0.15)
    print("                    P&!~^^?BP~^           .#& :~.  .^  .            G&: ::?&B5~                     ")
    time.sleep(0.15)
    print("                    #&?J?JY?   .           Y@..^?:.~?.  .          .@!  ^G&&#!                      ")
    time.sleep(0.15)
    print("                     !GJY??J~:.J.          Y@.  !. :^  .::        .#&?.:P#G?.                       ")
    time.sleep(0.15)
    print("                        ^!Y!7.7^!7~:       .@5 .?. .   ! ..    .7?YP!P7~~.                          ")
    time.sleep(0.15)
    print("                                            !@^ 7:.                                                 ")
    time.sleep(0.15)
    print("                                             7@!                                                    ")
    time.sleep(0.15)
    print("                                              Y&~                                                   ")
    time.sleep(0.15)
    print("                                               ^&7                                                  ")
                    
clear()
cicada()

print("Hello.")
time.sleep(1)
print()
print("We are looking for highly intelligent individuals.", end = time.sleep(0.75)) 
print("To find them, we have devised a test.")
time.sleep(0.1)
print("\n")
print("There is a message hidden in this room.")
time.sleep(1)
print("Find it, and it will lead you on the road to finding us.")
time.sleep(1)
print("We look forward to meeting the few that will make it all the way through.")
time.sleep(1)
print("\n")
print("Good luck.")
time.sleep(1)
print("\n")
print("3301")
print()
input("Press enter to accept challenge...")

intro = True
while intro:
    clear()
    time.sleep(0.75)
    print("Are you prepared to undertake this journey?")
    ans = input("(Yes or No): ")
    time.sleep(0.75)
    print("\n")
    if ans.lower() == "no" or ans.lower() == "n":
        print("blah blah blah who are you etc")
        time.sleep(0.75)
        print("more info etc")
        time.sleep(0.75)
        print("more info")
        intro = False
    elif ans.lower() == "yes" or ans.lower() == "y":
        print("We'll see about that...")
        intro = False
    else:
        print("You either understand or you don't.")
print("\n")
time.sleep(1)
playername = input("What is your digital alias? ")
time.sleep(1)
while playername == "" or playername == " " or playername.lower() == "cicada":
    playername = input("Invalid. Try again.")
time.sleep(1)
print(playername + " has been successfully added to player database.") # change this


# Function for inserting the player name the eye
def formatName(playername, length):
    nameLen=len(playername)
    if nameLen>length:
        return "X"*length
    r = length % nameLen
    m = length//nameLen
    names = m * playername
    if 2 % 2 == 0: #even Xs
        return "X"*(r//2) + names + "X" * (r//2)
    else: #odd Xs
        return "X"+"X"*(r//2)+names+"X"*(r//2)




#print()
# do something cool with the players name
# add music

print("\n")
time.sleep(1)
print("Remember")
time.sleep(1)
print("\n")
print("Cicada sees all.")
time.sleep(1)
print("Cicada knows all.")
time.sleep(1)
print("Break the rules,", playername, ",", "and I will find out.")
time.sleep(1)

eye()


time.sleep(0.75)

input("Press enter to continue...")

player = Player(playername)


printSituation()

player.location = pdx
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False

    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        
        while command == " " or command == "":
            command = input("What now? ")

        commandWords = command.split()
        
        # go
        if commandWords[0].lower() == "go":   # cannot handle multi-word directions
            player.goDirection(commandWords[1].lower()) 
            timePasses = True

        # pickup
        elif commandWords[0].lower() == "pickup":  # can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
                timePasses = True
            else:
                print("No such item.")
                commandSuccess = False


        # add other commands! 

        # inventory
        elif commandWords[0].lower() == "inventory":
            player.showInventory()        

        # help
        elif commandWords[0].lower() == "help":
            showHelp()

        # exit
        elif commandWords[0].lower() == "exit":
            playing = False

        # attack
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        # fly to
        #if commandWords[0].lower() == "fly to" or commandWords[0].lower() == "fly":
        #    targetName = command
        # invalid command
        else:
            print("Not a valid command.")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    



