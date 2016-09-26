######################################################################
# Name: George Cazenavette, James Pagnutti, Olivia Spears
# Date: 4/5/2016
# Description: RoomGame Reloaded
######################################################################

#We added two floors below the original floor (3 dimensions)
#Total of 8 room
#Player can now win the game by taking the key to the chest and getting the ladder
#Item descriptions now change after the related grabbable is taken
#Added items to all the additional rooms
#Rooms wil now change images after an item is taken from them (except for the chest room)


######################################################################
from Tkinter import *

# the blueprint for a room
class Room(object):
    # constructor
    def __init__(self, name, floor, image): #added a third parameter for floor
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)

        self.name = name
        # NEW
        self.image = image
        # NEW CODE!!! This is an instance variable for the floor of the room
        self.floor = floor 
        # exits are now stored in a dictionary
        self.exits = {}
        # items are now stored in a dictionary
        self.items = {}
        self.grabbables = []
        # NEW CODE!!! This is an instance variable for the current description index of the room
        self.imageIndex = 0
        # It allows for an item description to have multiple parts that can be split apart
        self.descIndex = 0

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # NEW
    @property
    def image(self):
        return self._image

    #NEW
    @image.setter
    def image(self, value):
        self._image = value
    
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
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

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

        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)

    
    def addItem(self, name, desc):
        # append the item and description to the appropriate lists
        self._items[name] = desc

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
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room

        s += "Exits: "

        for exit in self.exits.keys():
            s += exit + " "

        return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)
    # creates the rooms
    def createRooms(self):
        r1 = Room("Room 1", "2", ["r1_key.gif", "r1_nokey.gif"])
        r2 = Room("Room 2", "2", ["r2.gif"])
        r3 = Room("Room 3", "2", ["r3_book.gif", "r3_nobook.gif"])
        r4 = Room("Room 4", "2", ["r4_pack.gif", "r4_nopack.gif"])
        r5 = Room("Room 5", "1", ["r5.gif"])
        global r6
        r6 = Room("Room 6", "1", ["r6.gif", "r6.gif"])
        r7 = Room("Room 7", "1", ["r7.gif"])
        r8 = Room("Room 8", "1", ["r8.gif"])

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
        r2.addItem("rug", "It's just a rug.  Just a regular rug.  Nothing to see here.")
        r2.addItem("fireplace", "It is very hot.  You really shouldn't touch it...  Aaaaaand you touched it.  You lose 5 points or something.")

        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addExit("down", r7)
        r3.addItem("bookshelves", "Oh dear.  Don't look at that.&Oh dear.  Don't look at that.")
        r3.addItem("statue", "Somebody made a life choice. ( ._.)&Somebody made a life choice. ( ._.)")
        r3.addItem("desk", "Fine.  I guess you can take one 'book'&Fine.  I guess you can take one 'book'")
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
        # new item
        r6.addItem("chest", "It is locked.  What if you had a key&You use your key on the chest.  It just so happens to contain a rope 'ladder' long enough to reach the ground from a second-story window.  How specific.&You already took the ladder. The chest is empty.")

        r7.addExit("north", r5)
        r7.addExit("east", r8)
        r7.addExit("up", r3)
        # new item
        r7.addItem("lamp", "It's a nice lamp.  It makes you feel happy inside.")

        r8.addExit("west", r7)
        r8.addExit("north", r6)
        # new item
        r8.addItem("coffee_table", "There is a coffee table.  Just a regular coffee table.")
        Game.currentRoom = r1

        Game.inventory = []
    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
        
    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            if Game.inventory.count("ladder") == 1:
                Game.img = PhotoImage(file="zoidberg.gif")
            else:
                # if dead, set the skull image
                Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image[Game.currentRoom.imageIndex])
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img


    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            if Game.inventory.count("ladder") == 1:
                # WINNER
                Game.text.insert(END, "You escaped the house through the window using your ladder.\nYou discover that you have been Dr. John Zoidberg the whole time.\nYou have transcended reality.\nYou win.")
            else:
                # if dead, let the player know
                Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
                "\nYou are carrying: " + str(Game.inventory) +\
                "\n\n" + status)
        Game.text.config(state=DISABLED)


    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"\
            or action == "sionara!"):
            exit(0)
        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
        # clear the player's input
            Game.player_input.delete(0, END)
            return
        # split the user input into words (words are separated by
        # spaces) and store the words in a list
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
                if (noun in Game.currentRoom.exits):
                    # if one is found, change the current room to
                    # the one that is associated with the
                    # specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]

                    # set the response (success)
                    response = "Room changed."
                    # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the
                    # item's description
                    response = Game.currentRoom.items[noun].split("&")[Game.currentRoom.descIndex]
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current
                # room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's
                        # inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the
                        # room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable
                        # items
                        Game.currentRoom.descIndex += 1
                        Game.currentRoom.imageIndex += 1
                        if noun == "key":
                            r6.addGrabbable("ladder")
                            r6.descIndex += 1
                        break
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


        
##########################################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
