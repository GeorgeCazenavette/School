from Tkinter import *
import time
import random
import pygame

# team names
# you should name the GIFs and WAVs after the team names if you use this challenge again
# ( ._.)
NAMES = ['GLADOS', 'CONKER', 'SHADOW', 'FUNKY KONG', 'ROB', 'BOWSER', 'KIRBY', 'SHODAN']

# starts pygame... This caused many problems...
pygame.init()

# constants and booleans used in the game
PLAYING = True
GAME_STARTED = False
TEAMS = []
DEFAULT_SCORE = 5000
# keeps track of whose turn it is
CURRENT_TEAM = 0
TIMER_START = 0
# keeps track of which round it is
ROUNDS = 1
# maximum number of rounds
MAX_ROUNDS = 5
# time given for each turn
ROUND_DELAY = 60
# font
# This is a special font where each character is the same width.
FONT = "Consolas"
# font sizes...
BUTTON_FONT_SIZE = 32
STANDINGS_FONT_SIZE = 18
LAST_BUTTON_PRESSED_FONT_SIZE = 36
STANDINGS_ORDER_FONT_SIZE = 24

# song that plays at the beginning of the game
STARTING_SONG = "dummy.wav"

# used to rank teams
sortedByScore = []

# initialized as a blank
lastButtonPressed = ""



# created Team objects for each team
# includes score, name, image, and theme song
def createTeams():
    for name in NAMES:
        TEAMS.append(Team(name, DEFAULT_SCORE, name + '.gif', name + '.wav'))
    random.shuffle(TEAMS)


def updateStandings():
    global sortedByScore
    # this lambda function returns each team's score as the item to be compared by the sorted function
    # the reverse = True sorts them highest to lowest
    sortedByScore = sorted(TEAMS, key=lambda t: t.score.get(), reverse = True)

    # assigns each team a rank based on the sortedByScore list
    for t in sortedByScore:
        t.rank = sortedByScore.index(t)+1

    # checks for ties and adjusts the ranks accordingly
    for i in range(1,8):
        if sortedByScore[i].score.get() == sortedByScore[i-1].score.get():
            sortedByScore[i].rank = sortedByScore[i-1].rank
    
    # creates the standings label
    standings = "Team\t\tScore\t\tRank\n"
    for t in TEAMS:
        # decides how many tabs to put in the standings string for each team
        # creates the standings label
        if (len(t.name) > 8):
            standings += "%s\t%s\t\t%s\n"%(t.name, t.score.get(), t.rank)
        else:
            standings += "%s\t\t%s\t\t%s\n"%(t.name, t.score.get(), t.rank)

    app.standingsLabel.config(text = standings)
            
    

class Team(object):
    def __init__(self, team_name, score, img, theme):
        self.name = team_name
        # IntVar allows us to easily update widgets
        self.score = IntVar(window)
        self.score.set(score)
        # loads each team's picture
        self.image = PhotoImage(file = img)
        

        # loads each team's theme song
        try:
            self.themeSong = pygame.mixer.Sound(theme)
        # raises this error message if the file isn't loaded
        except:
            raise UserWarning, "{} sound files could not be loaded.".format(theme)
        
    # used this for debugging
    def __str__(self):
        print self.name

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # makes these rows expand to fill the screen
        master.rowconfigure(7, weight = 1)
        master.rowconfigure(8, weight = 1)

        # makes these columns expand to fill the screen
        for i in range (4):
            master.columnconfigure(i, weight = 1)

        # plays starting song
        self.startSong = pygame.mixer.Sound(STARTING_SONG)
        # plays until stopped
        self.startSong.play(-1)
   
    # resets the timer clock to the current time
    def reset_clock(self):
        self.startTime = time.time()

    # tick the clock
    def update_clock(self):
        if (GAME_STARTED):
            # remaning time is calculated
            remaining = ROUND_DELAY - (time.time() - self.startTime)
            self.timerLabel.config(text="TIME REMAINING\n{}".format(int(remaining+1)))
            self.timerLabel.config(fg = "black")
            
            # when there is 5s left warn the user with a red background
            if remaining <= 5:
                app.timerLabel.config(fg = "red")
                # when there is no time left, pick a random button and press it for the team
                if remaining <= 0:
                    buttons = {
                        0: button1action, 1: button2action, 2: button3action, 3: button4action, 4: button5action, 5: button6action, 6: button7action, 7: button8action
                    }

                    buttons[random.randint(0, 7)]()
        
        # if the game is active, recursively call this function after ~0.5s
        if (PLAYING): 
            self.master.after(485, self.update_clock)
        
    def setupGUI(self):
        # title label
        label1 = Label(self.master, text="PROJECT: BUTTON",font = (FONT, 32, "bold") )
        label1.grid(row=0, column=0, columnspan=4)
        
        # dictionary used while populating the grid
        gridPosition = {
            'x': 0,
            'y': 1
        }
        
        for t in TEAMS:
            # creates the team name label
            t.nameLabel = (Label(self.master, text=t.name, bg = "grey", font = FONT))
            t.nameLabel.grid(row=gridPosition['y'], column=gridPosition['x'], sticky = NSEW)
            
            # creates the team score albel
            t.scoreLabel = Label(self.master, textvariable = t.score, font = FONT)
            t.scoreLabel.grid(row=gridPosition['y']+1, column=gridPosition['x'], sticky = NSEW)

            # creates the team image label
            t.imageLabel = Label(self.master, image = t.image)
            t.imageLabel.grid(row=gridPosition['y']+2, column=gridPosition['x'], sticky = NSEW)

            # updates position on the grid
            gridPosition['x'] += 1
            
            # loops back around after the 4th column
            if gridPosition['x'] == 4:
                gridPosition['x'] = 0
                gridPosition['y'] += 3
            

        # creates all the buttons
        button1 = Button(self.master, text="A", command=button1action, font = (FONT, BUTTON_FONT_SIZE))
        button1.grid(row=7, column=0, sticky=NSEW)
        button2 = Button(self.master, text="B", command=button2action, font = (FONT, BUTTON_FONT_SIZE))
        button2.grid(row=7, column=1, sticky=NSEW)
        button3 = Button(self.master, text="C", command=button3action, font = (FONT, BUTTON_FONT_SIZE))
        button3.grid(row=7, column=2, sticky=NSEW)
        button4 = Button(self.master, text="D", command=button4action, font = (FONT, BUTTON_FONT_SIZE))
        button4.grid(row=7, column=3, sticky=NSEW)
        button5 = Button(self.master, text="E", command=button5action, font = (FONT, BUTTON_FONT_SIZE))
        button5.grid(row=8, column=0, sticky=NSEW)
        button6 = Button(self.master, text="F", command=button6action, font = (FONT, BUTTON_FONT_SIZE))
        button6.grid(row=8, column=1, sticky=NSEW)
        button5 = Button(self.master, text="G", command=button7action, font = (FONT, BUTTON_FONT_SIZE))
        button5.grid(row=8, column=2, sticky=NSEW)
        button6 = Button(self.master, text="H", command=button8action, font = (FONT, BUTTON_FONT_SIZE))
        button6.grid(row=8, column=3, sticky=NSEW)

        # creates the timer label
        self.timerLabel = Label(self.master, text = "TIME REMAINING\n0", font = (FONT, 24))
        self.timerLabel.grid(row=7, column=4, rowspan=2, columnspan = 2, sticky=N+E+W)
        

        # creates the stanings label
        self.standingsLabel = Label(self.master, justify = "left", font = (FONT, STANDINGS_FONT_SIZE))
        self.standingsLabel.grid(row = 1, column = 5, sticky = W+N, rowspan = 5)

        # shuffles the order of the teams
        random.shuffle(TEAMS)

        # updates the standings
        updateStandings()

        # creates the arrow that always points to the current team
        self.turnTracker = Label(self.master, text = "\n➔", justify = "right", font = (FONT, STANDINGS_FONT_SIZE))
        self.turnTracker.grid(row = 1, column = 4, sticky = E+N, rowspan = 5)

        # creates a label for the last button pressed
        self.lastButtonLabel = Label(self.master, text = "Last Button Pressed:\n", font = (FONT, LAST_BUTTON_PRESSED_FONT_SIZE))
        self.lastButtonLabel.grid(row = 5, column = 4, rowspan = 3, columnspan = 2, sticky = N+E+W)

        # Displays current round
        self.currentRoundLabel = Label(self.master, text = "Round 1", font = (FONT, STANDINGS_ORDER_FONT_SIZE))
        self.currentRoundLabel.grid(row = 0, column = 4, columnspan = 2)

        

        
# Button A
#   The player who clicks on it gets 2000 points
def button1action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    TEAMS[CURRENT_TEAM].score.set(TEAMS[CURRENT_TEAM].score.get()+2000)
    lastButtonPressed = "A"
    endTurn()
    
# Button B
#   Each team gets 500 points
def button2action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    for t in TEAMS:
        t.score.set(t.score.get()+500)
    lastButtonPressed = "B"
    endTurn()
    
# Button C
#   Each team loses score depending on their rank
def button3action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    for t in TEAMS:
        t.score.set(int(t.score.get() * ( t.rank / 8.0)))
    lastButtonPressed = "C"
    endTurn()
    
# Button D
#   The team who pressed it loses 3000 points
def button4action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    TEAMS[CURRENT_TEAM].score.set(TEAMS[CURRENT_TEAM].score.get()-3000)
    lastButtonPressed = "D"
    endTurn()
    
# Button E
#   Each team gets 500 * their rank points
def button5action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    for t in TEAMS:
        t.score.set(t.score.get() + 500 * t.rank)
    lastButtonPressed = "E"
    endTurn()
    
# Button F
#   The team who pressed it gets their score multiplied by 1.5
def button6action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    TEAMS[CURRENT_TEAM].score.set(int(TEAMS[CURRENT_TEAM].score.get() * 1.5))
    lastButtonPressed = "F"
    endTurn()
    
# Button G
#   Adds one point and gives a SMASH MOUTH SUPRISE
def button7action():
    global PLAYING
    if (not PLAYING):
        return True
    global lastButtonPressed
    TEAMS[CURRENT_TEAM].score.set(TEAMS[CURRENT_TEAM].score.get() + 1)
    # disable all theme songs
    for t in TEAMS:
        t.themeSong.set_volume(0)
    app.startSong.set_volume(0)
    pygame.mixer.Sound('all_star.wav').play()
    # Sleep for 3 seconds so that the clip can play out, and set 
    #  playing to false so no buttons can be pressed
    PLAYING = False
    time.sleep(3)
    PLAYING = True
    # enable all the theme songs
    for t in TEAMS:
        t.themeSong.set_volume(100)
    app.startSong.set_volume(100)
    lastButtonPressed = "G"
    endTurn()
    
# Button H
#   Swaps a random team and the current teams scores.
def button8action():
    if (not PLAYING):
        return True
    global lastButtonPressed
    otherTeam = random.randint(0,7)
    while (TEAMS[otherTeam] == CURRENT_TEAM):
        otherTeam = random.randint(0,7)
    tempScore = TEAMS[otherTeam].score.get()
    TEAMS[otherTeam].score.set(TEAMS[CURRENT_TEAM].score.get())
    TEAMS[CURRENT_TEAM].score.set(tempScore)
    lastButtonPressed = "H"
    endTurn()

# After every button press, setup the new turn
def endTurn():
    global GAME_STARTED
    GAME_STARTED = True
    global CURRENT_TEAM
    global ROUNDS
    global TEAMS
    TEAMS[CURRENT_TEAM].nameLabel.config(bg = "grey", fg="black")
    # If the current team is at 7, then the round is over, and a new team
    #    order is generated and new theme song plays
    if CURRENT_TEAM == 7:
        ROUNDS += 1
        app.currentRoundLabel.config(text = "Round %s"%(ROUNDS))
        CURRENT_TEAM = -1
        app.startSong.stop()
        for t in TEAMS:
            t.themeSong.stop()
        # order the teams by their score and then plays the first place team's theme song
        sorted(TEAMS, key=lambda t: t.score.get(), reverse = True)[0].themeSong.play(-1)
        random.shuffle(TEAMS)
    
    # When the game reaches its last round, display game over.
    if (ROUNDS > MAX_ROUNDS):
        global PLAYING
        PLAYING = False
        app.currentRoundLabel.config(text = "GAME OVER")
        # order the teams by their score to display at the end of the game
        TEAMS = sorted(TEAMS, key=lambda t: t.score.get(), reverse = True)
    else:
        CURRENT_TEAM += 1
        
    
    # Sets the current teams label to red, so that it lets the user know whose turn it is
    TEAMS[CURRENT_TEAM].nameLabel.config(fg="red", bg = "black")
    updateStandings()
    app.turnTracker.config(text = "\n"*(CURRENT_TEAM+1) + "➔")
    app.lastButtonLabel.config(text = "Last Button Pressed:\n%s"%(lastButtonPressed))
    app.reset_clock()
    
################################################################################
# The main part of the program 
################################################################################

window = Tk()
# created the teams
createTeams()

# makes the GUI fullscreen
window.attributes("-fullscreen", True)
# creates the App
app = App(window)
# sets up the GUI
app.setupGUI()
app.reset_clock()
app.update_clock()
# highlights the curent team's label
TEAMS[CURRENT_TEAM].nameLabel.config(fg="red", bg = "black")
window.mainloop()
# stops playing music when the GUI is closed
pygame.quit()
