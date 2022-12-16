from room import Room 
# can add other classes
#from room import Barrier, quizBarrier
from player import Player
from item import * # other item classes as well
from monster import Monster
from NPC import NPC #, Cicada
import os
import updater
import time
import sys


beatCicada = False

# creating rooms (aka cities) - and subrooms (aka puzzles) #

# home city = pdx
pdx = Room("Home", "Portland, OR, where you live on Reed College campus.")
p1 = Room("Puzzle 1", "blah")
p2 = Room("Puzzle 2", "bleh")
p3 = Room("Puzzle 3", "bloh") 
    
### 
    
# seoul, south korea 
sol = Room("Seoul", "You are now in South Korea...")
s1 = Room("Puzzle 4", "bleeh")
s2 = Room("Puzzle 5", "blaeugh")
s3 = Room("Puzzle 6", "bleooaun")


###

# warsaw, poland
war = Room("Warsaw", "You are now in Poland...")
w1 = Room("Puzzle 7", "blafhdj")
w2 = Room("Puzzle 8", "blahshsh")

###

# haleiwa, hawaii
hal = Room("Haleiwa", "You are now in Hawaii...")
h1 = Room("Puzzle 9", "bleaosy")
h2 = Room("Puzzle 10", "blaaksns")

#connects all cities to each other
cities = [pdx, sol, war, hal]
for i in cities:
    for k in cities:
        if len(k.exits)==0 and k!=i:
            flyout = "fly to " + str(k.location)
            flyback = "fly back " + str(i.location)
            Room.connectRooms(i, flyout, k, flyback)
    

# connecting rooms to puzzles #
Room.connectRooms(pdx, "forward", p1, "backward")
Room.connectRooms(p1, "forward", p2, "backward")
Room.connectRooms(p2, "forward", p3, "backward")
Room.connectRooms(p3, "forward", pdx, "backward")
Room.connectRooms(sol, "forward", s1, "backward")
Room.connectRooms(s1, "forward", s2, "backward")
Room.connectRooms(s2, "forward", s3, "backward")

    #Room.connectRooms(p1, "")

    ## seoul 
    # Room.connectRooms(p1, " ", p2, " ")
    #Room.connectRooms(ekv, "east", hal, "west")
    #Room.connectRooms(sol, "north", r3, "south")
    #Room.connectRooms(r2, "north", r4, "south")

    ###

# creating items #

i = Books("Booky book", "Just a book", 1, Player)


# creating monsters #
#Monster("Bob the monster", pdx)

###

# creating NPCs #

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation(player):
    
    clear()

    #player.showStatus              #redundant with below
    #print(player.location.desc)    #
    time.sleep(0.2)
    print("\n")
    print("Your intelligence: " + str(player.intelligence))
    print("Your health: " + str(player.health))
    print("Your location: " + str(player.location.desc))
    print("Your level: " + str(player.level))
    print("\n")
    # monsters
    if player.location.hasMonsters():
        print("This room contains the following monster(s): \n")
        for m in player.location.monsters:
            time.sleep(0.5)
            print(m.name)
        print("\n")
    
    # items
    if player.location.hasItems():
        print("This room contains the following items: \n")
        for i in player.location.items:
            time.sleep(0.5)
            print(i.name)
        print("\n")
    else:
        print("This room contains no items...")
        print("\n")
        
    # characters
    if player.location.hasCharacters():
        print("This room contains the following characters: \n")
        for i in player.location.characters:
            time.sleep(0.5)
            print(i.name)
        print("\n")

    # barriers
    if player.location.hasBarriers():
        print("This room contains the following obstacles: \n")
        for i in player.location.barriers:
            time.sleep(0.5)
            print(i.name) 
        print("\n")

    #this is currently faulty - change it to be more clean
    print("You can go in the following directions: \n")
    for exit in player.location.exitNames():
        print(exit)
    print("\n")
    # anything extra


# help screen (make this cool and meta and stuff)
def showHelp():
    clear()
    print("\n")
    print("Cicada 3301: Remember. There are 10 puzzles. You cannot move on unless you answer correctly.")
    print("help -- brings up this help screen")
    print("go <forward/backward> -- moves you in the given direction onto the next puzzle")
    print("inventory -- opens your inventory") # make inventory cool
    print("inspect <item or npc> -- gives you a short description of the item or NPC")
    #print("eat <item> -- ")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops the item")
    print("use <item> -- uses an item. Also works to read an item.") #separate the read function from the use one
    print("status -- shows your current status")
    print("attack <monster> -- attacks chosen monster")
    # have these been coded yet?
    print("talk to <NPC> -- talks to an NPC")
    print("\n")
    print("Getting low on health?")
    print("There are various food-like items in the game - type the eat command and see what happens!")
    print("Getting low on intelligence?")
    print("Read a book. Come on, what did you expect?")
    input("Press enter to continue...")
    print("\n")



# # # # # # # # # # # #





### intro scene ###
# add music
# print cicada intro

# Some cool ASCII printing functions
"""
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
"""
# cleared for speed
clear()
#cicada()
# # # # # # # # # # # # #
def endings():
    clear()

    pass



# # # # # # # # # # # # # remember to remove commented out paragraphs

"""
# cicada 3301 screen

clear()
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
"""

intro = False
while intro:
    clear()
    time.sleep(0.75)
    print("Are you prepared to undertake this journey?")
    ans = input("(Yes or No): ")
    time.sleep(0.75)
    print("\n")
    if ans.lower() == "no" or ans.lower() == "n":
        print("You are a regular, boring person browsing reddit in 2012 when you find out about this strange internet phenomenon called Cicada 3301.")
        time.sleep(0.75)
        print("Since you already spend too much time online, you decide to investigate.")
        time.sleep(0.75)
        print("Nobody knows who is behind the cryptic puzzles being released on the internet...")
        time.sleep(0.75)
        print("But maybe you will be the one to find out...")
        time.sleep(0.25)
        print("How?")
        time.sleep(1)
        print("You will travel the world, answering puzzles and fighting your enemies with words and books and stuff...")
        time.sleep(0.75)
        print("To find out who Cicada truly is, you can increase your intelligence by reading books, which helps you answer all 10 puzzles.")
        time.sleep(0.75)
        print("You must keep your health up by eating food.")
        time.sleep(0.1)
        print("And make sure your intelligence stays high, and your criminal activity doesn't...")
        time.sleep(0.75)
        print("Or you die :(")
        time.sleep(1)
        print("Cicada will be watching. Type help to see the list of commands.")
        time.sleep(0.25)
        intro = False
    elif ans.lower() == "yes" or ans.lower() == "y":
        print("Are you sure? We will see about that...")
        time.sleep(0.75)
        print("Remember, you can type help to see a list of the commands.")
        intro = False
    else:
        print("You either understand or you don't.")
print("\n")
time.sleep(1)
playername = input("What is your alias? ")

while playername == "" or playername == " " or playername.lower() == "Cicada":
    playername = input("Smart. It's good to be private about these things. Unfortunately we need an answer: ")

jimcheck=playername
if "jim" in jimcheck.lower():
    print ("hi jim I hope u like our final :)")
for x in range (0,5):  
    b = "Processing" + "." * x
    print (b, end="\r")
    time.sleep(0.25)
print(playername + " has been successfully added to player database.") 
time.sleep(1)
input("You may now enter")

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
# commented out for speed
"""
print("\n")
time.sleep(1)
print("Remember")
time.sleep(1)
print("\n")
print("Cicada sees all.")
time.sleep(1)
print("Cicada knows all.")
time.sleep(1)
print("You will hear from me throughout the game")
print("\n")
time.sleep(0.5)
print("Cicada 3301: Just like this")
print("\n")
time.sleep(0.5)
print("Cicada 3301: Break the rules,", playername,"...")
time.sleep(0.75)
print("and I will find out.")
time.sleep(1)

eye()

time.sleep(0.75)
"""

#input("Press enter to continue...")



""" creating the world """
player = Player(playername)
i = Item(player,"Guide to Cicada 3301", "This is a copy of the game's instructions.", 3)
i.putInRoom(pdx)

# GAME STARTS HERE

# add conversation

player.location = pdx

playing = True

while playing and player.alive:
    if player.location == h2:
        # special final boss thing
        pass
    printSituation(player)
    commandSuccess = False
    timePasses = False

    while not commandSuccess:
        commandSuccess = True
        needsHelp=False
        command = input("What do you want to do now? ")
        while command == " " or command == "":
            command = input("What do you want to do now? ")
        commandWords = command.split()
            
        # add other commands! 

        # exit
        if commandWords[0].lower() == "exit":
            playing = False

        # help
        elif commandWords[0].lower() == "help":
            showHelp()

        # go
        elif commandWords[0].lower() == "go": 
            # cannot handle multi-word directions
            player.goDirection(commandWords[1].lower()) 
            timePasses = True

        # pickup
        elif commandWords[0].lower() == "pick" or commandWords[0].lower() =="pickup":  # can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
                timePasses = True
            else:
                print("No such item.")
                commandSuccess = False

        # use - make sure to separate from read and eat if we have time
        elif commandWords[0].lower() == "use":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target in player.items:
                player.useitem(target) # has this been coded
                timePasses = True
            else:
                print("You don't have that item in your inventory!")
                commandSuccess = False

        # drop
        elif commandWords[0].lower() == "drop":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            
            if target in player.items:
                player.dropoff(target)
            else:
                print("You do not have this item.")
                commandSuccess = False

        # inventory
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
                
        # inspect 
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            description = targetName.desc
            if description:
                print (description)
            elif description == False:
                print("The item you seek does not exist.")
                commandSuccess = False
                input("Press enter to continue...")

        # status
        elif commandWords[0].lower() == "status" or commandWords[0].lower() == "me":
            player.showStatus() 

        # wait 
        elif commandWords[0].lower() == "wait":
            timePasses= True


        # attack
        #elif commandWords[0].lower() == "attack":
        #    targetName = command[7:]
        #    target = player.location.getMonsterByName(targetName)
        #    if target != False:
        #        player.attackMonster(target)
        #    else:
        #        print("No such monster.")
        #        commandSuccess = False

        # fly to
        if player.level > 5:
            clear()
            print("Congratulations. You have successfully unmasked Cicada. The world of cryptography and computation has been forever changed.")
            time.sleep(5)
            print ("Dei spectant.")
            time.sleep(2)
            clear()
            print ("Dei spectant.")
            time.sleep(3)
            clear()
            time.sleep(1)
            quit()
        
        if commandWords[0].lower() == "fly to" or commandWords[0].lower() == "fly":
            if commandWords[0].lower() == "fly to":
                x = 8
            else:
                x=4
            player.goDirection(commandWords[1].lower()) 
            timePasses = True
        
        else:
            if not player.needsHelp:
                print("Not a valid command.")
                player.needsHelp=True
            else:
                print("Not a valid command. You may always ask for help.")
                player.needsHelp=False
            commandSuccess = False
            
    if timePasses == True:
        updater.updateAll()