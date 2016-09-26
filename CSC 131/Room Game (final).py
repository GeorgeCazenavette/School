######################################################################
# Name: George Cazenavette, James Pagnutti, Olivia Spears
# Date: 2/5/2016
# Description: RoomGame
######################################################################

#We added two floors below the original floor (3 dimensions)
#Total of 12 room
#Player can now win the game by taking the key to the chest and getting the ladder
#Item descriptions now change after the related grabbable is taken
#Added items to all the additional rooms


######################################################################
# the blueprint for a room
class Room(object):
    # constructor
    def __init__(self, name, floor): #added a third parameter for floor
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        # NEW CODE!!! This is an instance variable for the floor of the room
        self.floor = floor 
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        # NEW CODE!!! This is an instance variable for the current description index of the room
        # It allows for an item description to have multiple parts that can be split apart
        self.descIndex = 0

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
        
    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def descIndex(self):
        return self._descIndex

    @descIndex.setter
    def descIndex(self, value):
        self._descIndex = value
        
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    
    def addItem(self, name, desc):
        # append the item and description to the appropriate lists
        self._items.append(name)
        self._itemDescriptions.append(desc)

    def delItem(self, name): #new function to remove items and their descriptions
        self._itemDescriptions.pop(self._items.index(name))
        self._itemDescriptions.remove(name)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)
        
      

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        # NEW CODE!!! Added the floor of the room.
        s = "You are in {}, Floor {}.\n".format(self.name, self.floor)

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "

        for exit in self.exits:
            s += exit + " "

        return s

#creates the rooms
#NEW CODE!!!! Added two 
def createRooms():
    # r1 through r12 are the twelve rooms in the mansion
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r4)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom

    # create the rooms and give them meaningful names
    # NEW CODE!!! The second parameter is the floor of the room
    r1 = Room("Room 1", "2")
    r2 = Room("Room 2", "2")
    r3 = Room("Room 3", "2")
    r4 = Room("Room 4", "2")
    r5 = Room("Room 5", "1")
    r6 = Room("Room 6", "1")
    r7 = Room("Room 7", "1")
    r8 = Room("Room 8", "1")
    global r9 #this room had to be globally accessable for the purpose of unlocking the chest
    r9 = Room("Room 9", "0")
    r10 = Room("Room 10", "0")
    r11 = Room("Room 11", "0")
    r12 = Room("Room 12", "0")

    # add exits to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    # add items to room 1
    r1.addItem("chair", "A very weird chair...  It almost looks like a---&A very weird chair...  It almost looks like a---")
    r1.addItem("table", "It looks like someone ate here... and left their 'key' ( ._.)&There is no longer a key here.  The food crumbs are still there though.")
    # add grabbables to room 1
    r1.addGrabbable("key")

    # This same process is repeated for the other rooms
    r2.addExit("south", r4)
    r2.addExit("west", r1)
    r2.addExit("down", r6)
    r2.addItem("rug", "It's just a rug.  Just a regular rug.  Nothing to see here.")
    r2.addItem("fireplace", "It is very hot.  You really shouldn't touch it...  Aaaaaand you touched it.  You lose 5 points or something.")

    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addItem("bookshelves", "It is empty.  Somebody dumb lives here.  I hope it isn't you.&It is empty.  Somebody dumb lives here.  I hope it isn't you.")
    r3.addItem("statue", "It looks weird.  Kind of like somebodyI know.&It looks weird.  Kind of like somebodyI know.")
    r3.addItem("desk", "It is a desk.  There is a 'book' here.  Thank God you at least own one book.&Now that you took the book, it's just a desk.")
    r3.addGrabbable("book")

    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)
    r4.addItem("brew_rig", "It's a brew rig.  Gourd likes brew rigs.  Someone left you a '6-pack'&The brew rig is still there, but the 6-pack is not")
    r4.addGrabbable("6-pack")

    r5.addExit("east", r6)
    r5.addExit("south", r7)
    # new item
    r5.addItem("chandelier", "It looks very pointy.  Hopefully It doesn't fall on you.")

    r6.addExit("south", r8)
    r6.addExit("west", r5)
    r6.addExit("up", r2)
    # new item
    r6.addItem("coffee_table", "There is a coffee table.  If only there were a coffee table book...")

    r7.addExit("north", r5)
    r7.addExit("east", r8)
    r7.addExit("down", r11)
    # new item
    r7.addItem("lamp", "It's a nice lamp.  It reminds you of what it felt like to see light and feel warmth.")

    r8.addExit("west", r7)
    r8.addExit("north", r6)
    # new item
    r8.addItem("plant", "What a nice potted plant.  It's amazing that anything could survive in this house.  Wait, nevermind.  It's fake.")

    r9.addExit("east", r10)
    r9.addExit("south", r11)
    # new item
    r9.addItem("chest", "It is locked.  What if you had a key?&You use your key on the chest.  It just so happens to contain a rope 'ladder' two stories long.&You already took the ladder.  The chest is empty.")

    r10.addExit("west", r9)
    r10.addExit("south", r12)
    # new item
    r10.addItem("MightyThirstyTM", "AS SEEN ON TV, IT'S THE MIGHTY THIRSTY! PERFECT FOR ANY SPILL!")

    r11.addExit("north", r9)
    r11.addExit("east", r12)
    r11.addExit("up", r7)
    # new item
    r11.addItem("sock", "There is a sock on the floor.  Where could the other one be?")

    r12.addExit("west", r11)
    r12.addExit("north", r10)
    # new item
    r12.addItem("the_other_sock", "You found the other sock.  Yay?  Why did you even want this sock?  No, you cannot take it.")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
               
# NEW CODE!!! Plays this message when the user wins the game.
def win():
    print("""                              ,oooooo888888888oooooo.
                         .oo88^^^^^^            ^^^^^Y8o.
                      .dP'                              `Yb.
                    dP'                                   `Yb 
                  .dP'                                     `Yb.
                 dP'                                         `Yb
                d8                                             8b
               ,8P                                             `8b
               88'                                              88
               88                                               88
               dP                                               88
              d8'                                               88
              8P                                               ,dY
            ,dP                                                88'
           CP   ,,.....                ,,.....                 88 
           `b,d8P'^^^'Y8b           ,d8P'^^^'Y8b.             ,dY
            dP'         `Yb        dP'         `Yb            88'
           dP             Yb      dP             Yb           88 
          dP     db        Yb    dP     db        Yb         ,dY
          88     YP        88    88     YP        88         88'
          Yb               dP    Yb               dP         88 
           Yb             dP      Yb             dP         ,dY
          dP`Yb.       ,dP'        `Yb.       ,dP'          88'
         CCo_ `YbooooodP'            `YbooooodP'            88
          dP"oo_    ,dP            Ybo__                    88
         88    "ooodP'                ""88oooooP'           88
          Yb .ood""                                        ,dY
          ,dP"                                             88'
        ,dP'                                               88
       dP'    ,dP'     ,dP       ,dP'      .bmw.           88
      d8     dP       dP        dP        o88888b          88
      88    dP       dP       ,dP       o8888888P          88
      Y8.   88      88       d8P       o8888888P          ,dY 
      `8b   Yb      88       88       ,8888888P           88'
       88    Yb     Y8.      88       888888P'            88
       88    `8b    `8b      88       88                 ,dY 
       88     88     88      Yb.      Yb                 88'
       Y8.   ,Y8    ,Y8      ,88      ,8b                88
        `"ooo"`"oooo" `"ooooo" `8boooooP                ,8Y
            88boo__      """       """  ____oooooooo888888
           dP  ^^""ooooooooo..oooooo\"""^^^^^             88
           88               88                           88
           88               88                           88 
           Yboooo__         88          ____oooooooo88888P
             ^^^\"""ooooooooo''oooooo\"""^^^^^""")
    print("You escaped the house through the window using your ladder.\nYou discover that you have been Dr. John Zoidberg the whole time.\nYou have transcended reality.\nYou win.")
          
def death():
    print " " * 17 + "u" * 7
    print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
    print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
    print " " * 9 + "u" + "$" * 21 + "u"
    print " " * 8 + "u" + "$" * 23 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +"\"" + " " * 3 + "\"" + "$" * 6 + "u"
    print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7+ "$" * 4 + "\""
    print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +"$" * 3
    print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
    print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +"$" * 3 + "u" * 2 + "$" * 4 + "\""
    print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
    print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
    print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
    print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"* 2 + " " * 7 + "u" * 3
    print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
    print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +"\"" + " " * 5 + "u" * 2 + "$" * 6
    print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +"u" * 4 + "$" * 10
    print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2+ "$" * 9 + "\"" * 3 + "$" * 3 + "\""
    print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +" " + "\"" * 2 + "$" + "\"" * 3
    print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
    print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +" \"\"" + "$" * 11 + "u" * 3 + "$" * 3
    print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *11 + "\""
    print("You fell out the window and died.\nYou lose.")


# main part of program

inventory = []  # nothing in inventory...yet
createRooms()   # create the rooms

#play forever
while (True):
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    # set the status so the player has situational awareness
    # the status has room and inventory information
    # If the currentRoom is None, then the game is over
    # This only happens if the player goes south from room 4
    if(currentRoom == None):
        # NEW CODE!!! If the player has the ladder, they win
        if (inventory.count("ladder") == 1):
            win()
        # NEW CODE!!! If the player does not have the ladder, they lose
        else:
            death()
        break

    # display the status
    print "============================================================"
    print status

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    # we use raw_input here to treat the input as a string instead of
    # an expression
    action = raw_input("What to do? ")
    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()
    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break


    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces)
    # and store the words in a list
    words = action.split()
    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
        # set a default response
            response = "Invalid exit."
            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break

        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "You cannot see that item."
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                # NEW CODE!!! This edit allows item names to have capital letters
                if (noun == currentRoom.items[i].lower()):
                    # set the response to the item's description
                    # NEW CODE!!!! Line edited to use the part of the description specified by the descIndex
                    response = currentRoom.itemDescriptions[i].split("&")[currentRoom.descIndex]
                    # no need to check any more items
                    break


        # the verb is: take
        elif (verb == "take"):
            # set a default response
            # NEW CODE!!! Changed this sentence to make more sense.
            response = "That is not a takable item"
            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # NEW CODE!!! Changes item descripions when a grabbable is grabbed
                    currentRoom.descIndex += 1
                    # NEW CODE!!! "Unlocks" the chest when the key is taken by incrementing the chest room's description index.
                    if (noun == "key"):
                        r9.descIndex += 1
                        r9.addGrabbable("ladder")
                    # add the grabbable item to the player's
                    # inventory
                    inventory.append(grabbable)
                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)
                    # set the response (success)
                    response = "Item grabbed."
                    # no need to check any more grabbable items
                    break


    # display the response
    # NEW CODE!!! Only displays the current room if the user is actually in a room
    if (currentRoom != None):
        print "\n{}".format(response)
