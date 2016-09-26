######################################################################################################################
# Name: George Cazenavette
# Date: 5/14/2016
# Description: Chaos Game Rainbow
######################################################################################################################
# imports Tkinter and random classes
from Tkinter import *
from random import randint

# the 2D point class
class Point(object):
    # added an instance variable for color with a default value of "#"
    # so that values can simply be appended to it
    def __init__(self, x=float(0), y=float(0), color = "#"):
        self.x = x
        self.y = y
        self.color = color

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
        self.create_oval(x, y, x + radius * 2, y + radius * 2, fill = color, outline = color)

    def play(self, NUM_POINTS):
        # creates the 3 verticies
        v1 = Point(WIDTH / 2, 10, "#ff0000")
        v2 = Point(10, HEIGHT - 10, "#00ff00")
        v3 = Point(WIDTH - 10, HEIGHT - 10, "#0000ff")
        # makes a list of the 3 verticies
        vert=[v1, v2, v3]
        # plots the verticies
        # added the instance variable for color
        for v in vert:
            self.plot(v.x-VERTEX_RADIUS, v.y-VERTEX_RADIUS, v.color , VERTEX_RADIUS)
            
        # calculates the average distance between the verticies
        average_distance = int((v1.dist(v2) + v2.dist(v3) + v3.dist(v1)) // 3)

        # chooses a random vertex to begin
        point = vert[randint(0,2)]
        for i in range(NUM_POINTS):
            # creates a point between the previous point and a random vertex
            point = point.midpt(vert[randint(0,2)])
            # adds color value based on distance from each vetex
            for j in range(3):
                # once it reaches halfway away from the vertex, it linearly depreciates in color
                if (point.dist(vert[j]) > average_distance / 2):
                    # calculates 8-bit color value
                    color_value = int(255 - ((point.dist(vert[j]) - average_distance / 2) * 255 / (average_distance / 2)))
                # if it is less than halfway away from the vertex, it gets the full color value
                else:
                    color_value = 255
                # stores the hex value of the color_value
                color_value_hex = str(hex(color_value))
                # appends the hex version of that color's value to the point's color
                if (color_value < 16):
                    # adds a "0" if the hex value is less than 10
                    point.color += "0" + color_value_hex[len(color_value_hex) - 1: len(color_value_hex)]
                else:
                    point.color += color_value_hex[len(color_value_hex) - 2: len(color_value_hex)]

            # plots the point with the calculated color value
            self.plot(point.x, point.y, point.color, POINT_RADIUS)
        
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
