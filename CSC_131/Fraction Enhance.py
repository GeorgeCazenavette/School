######################################################################################################################
# Name: George Cazenavette
# Date: 2/24/2016
# Description: Fraction Enhance
######################################################################################################################
from math import sqrt

class Fraction(object):
	# write your code for the fraction class here
    #initializes the object and provides default values
    def __init__(self, num = 0, den = 1):
        self.num = num
        #prevents the denominator from being 0
        if (den == 0):
            self.den = 1
        else:
            self.den = den     

    #num getter
    @property
    def num(self):
        return self._num

    #num setter
    @num.setter
    def num(self, value):
        self._num = value

    #num getter
    @property
    def den(self):
        return self._den

    #num setter
    @den.setter
    def den(self, value):
        #prevents den from being manually set to 0 (not done in this program)
        if (value == 0):
            print("you can't make a denominator 0...")
        else:
            self._den = value

    #returns a string form of the class for printing
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, float(self.num)/self.den)

    #adding method
    def __add__(self, other):
        #cross multiplies and adds to get num, multiplies both dens to get den
        return red(Fraction(other.den * self.num + self.den * other.num, self.den * other.den))

    #subtracting method
    def __sub__(self, other):
        #inverts the sign of the num of the second fraction then adds
        return self + Fraction(-1 * other.num, other.den)

    #multiplying method
    def __mul__(self, other):
        return red(Fraction(self.num * other.num, self.den * other.den))

    #division method
    def __div__(self, other):
        #inverts the num and dem of the second fraction then multiplies
        return self * Fraction(other.den, other.num)

#recursive function that continually reduces the fraction
def red(frac):
    #sets the fraction to 0/1 if the num is 0
    if (frac.num == 0):
        return Fraction()
    i = 2
    #looks for common factors up to the square root of the lesser number
    while (i <= sqrt(frac.num) and i <= sqrt(frac.den)):
        if (frac.num % i == 0 and frac.den % i ==0):
            #reduces the function by the common factor and calls the reduce function again
            return red(Fraction(frac.num / i, frac.den / i))
        i += 1
    return frac
         

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4
