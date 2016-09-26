###########################################################################################
# Name: George Cazenavette
# Date: 1/27/2016
# Description: Project Euler 3 & 4
###########################################################################################

# it may help to make use of some math functions (which you can import)
# it may also help to define other "helper" functions (i.e., delegate tasks!)


#NOTE: I added some code to calculate the runtime, but I commented out the lines
#      that print it because I was not sure if you would have wanted it.       

import math

import time



# solves problem 3
def problem3():
    #this function finds the prime factorization of the number while only storing the largest factor found
    #a prime checker is not necessary because the first factor found will always be prime
    num = 600851475143          #the number we are deconstructing
    div = 3                     #the initial divisor
    factor = 1                  #represents the largest found prime factor
    
    while num != 1:             #continues the loop until the number is compleely factored
        if (num % div == 0):    #checks if the number is divisible by the current divisor
            num = num / div     #if so, divides the number by the current divisor
            if (div > factor):  #checks if the found factor is greater than the largest found factor
                factor = div    #if so, stores it as the factor variable
            div = 1             #sets div to 1 so that "div += 2" will reset div to 3 once a factor has been found
        div += 2                #moves on to the next possible factor (skips even numbers)
    return factor               #returns the largest factor found
	

# solves problem 4
def problem4():
    #write your code below for this problem (and remove this comment...)
    pal = 1                     #initializes the palindrome variable
    for i in range (100,1000):
        for j in range (i,1000):#cycles through all multiples of 3 digit numbers
            prod = i * j

                                #checks to see if the multiple is a palindrome and if it is the largest found
            if ((prod > pal) & (str(prod) == str(prod)[::-1])): #(is selected slice cheating?)
                pal = prod      #if so, saves it as the largest palindrome
    return pal                  #returns the largest foudn palindrome

# the main part of the program

#initializes a start time so the runtime can be calculated
t=time.time()

#solves and prints problem 3
sol3 = problem3()
print "The largest prime factor of the number 600851475143 is {}".format(sol3)

#prints the runtime for problem3
#print ("runtime = " + str(time.time()-t))

#initializes a start time so the runtime can be calculated
t=time.time()

#solves and prints problem4
sol4 = problem4()
print "The largest palindrome made from the product of two 3-digit numbers is {}".format(sol4)

#prints the runtime for problem4
#print ("runtime = " + str(time.time()-t))
