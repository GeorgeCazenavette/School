######################################################################################################################
# Name: George Cazenavette
# Date: 3/14/2016
# Description: 
######################################################################################################################

# the 2D point class


class Point(object):
	# write your code for the point class here (and subsequently remove this comment)
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

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3
# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)
# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
