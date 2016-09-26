######################################################################################################################
# Name: George Cazenavette
# Date: 3/21/2016
# Description: 2D Points...Plotted
######################################################################################################################

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


# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    
    # constructor, calls canvas instructor, creates a blank, white canvas
    def __init__(self, master):
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)

    # creates a point object, alters its coordinates, and calls the plot function
    def plotPoints(self, n):
        point = Point()
        for i in range(n):
            # specified boundaries of the points
            point.x = randint(0, WIDTH - 1)
            point.y = randint(0, HEIGHT - 1)
            self.plot(point.x, point.y)

    def plot(self, x, y):
        # selects a random color from the list of colors
        color = COLORS[randint(0, len(COLORS) - 1)]
        # plots the colored point as an oval of radius zero
        self.create_oval(x, y, x + POINT_RADIUS * 2, y + POINT_RADIUS * 2, outline = color)
	

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
# the number of points to plot
NUM_POINTS = 2500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
