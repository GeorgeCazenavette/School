######################################################################################################################
# Name: George Cazenavette
# Date: 4/4/2016
# Description: Chaos Game
######################################################################################################################
# imports Tkinter and random classes
from Tkinter import *
from random import randint

# the 2D point class
class Point(object):
    def __init__(self, x=float(0), y=float(0)):
        self.x = x
        self.y = y

    #getter for x
    @property
    def x(self):
        return self._x

    #setter for x
    #forces float type
    @x.setter
    def x(self, value):
        self._x = float(value)

    #getter for y
    @property
    def y(self):
        return self._y

    #setter for y
    #forces float type
    @y.setter
    def y(self, value):
        self._y = float(value)

    #uses pythagorean theorem to find distance between 2 points
    def dist(self, other):
        return ( ( self.x - other.x ) ** 2 + ( self.y - other.y) ** 2 ) ** 0.5

    #finds average x and average y to compute midpoint
    def midpt(self, other):
        midx = ( self.x + other.x ) / 2
        midy = ( self.y + other.y ) / 2
        return Point(midx, midy)

    #returns a string form of a Point object
    def __str__(self):
        return "({},{})".format(self.x, self.y)	

# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):

    def __init__(self, master):
        # creates the white canvas
        Canvas.__init__(self, master, bg = "white")
        # allows it to expand
        self.pack(fill = BOTH, expand = 1)
        
    def plot(self, x, y, color, radius):
        # creates a circular point based on the arguments
        self.create_oval(x, y, x + radius * 2, y + radius * 2,fill = color, outline = color)

    def play(self, NUM_POINTS):
        # creates the 3 verticies
        v1 = Point(WIDTH / 2, 10)
        v2 = Point(10, HEIGHT - 10)
        v3 = Point(WIDTH - 10, HEIGHT - 10)
        # makes a list of the 3 verticies
        vert=[v1, v2, v3]
        # plots the verticies
        for i in vert:
            self.plot(i.x-VERTEX_RADIUS, i.y-VERTEX_RADIUS, VERTEX_COLOR, VERTEX_RADIUS)
        # chooses a random vertex to begin
        point = vert[randint(0,2)]
        for i in range(NUM_POINTS):
            # creates a point between the previous point and a random vertex
            point = point.midpt(vert[randint(0,2)])
            # plots that point
            self.plot(point.x, point.y, POINT_COLOR, POINT_RADIUS)
        
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT_COLOR = "black"
# the number of midpoints to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)
# wait for the window to close
window.mainloop()
