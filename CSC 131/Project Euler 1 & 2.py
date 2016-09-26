###########################################################################################
# Name: George Cazenavette
# Date: 19 January 2016
# Description: Project Euler 1 and 2
###########################################################################################

# solves problem 1
def problem1():
    summation = 0
    counter = 1
    #limits the counter to less than 1000
    while counter < 1000:
        #checks if the counter is divisible by 3 or 5 and if so adds it to the sum
        if counter % 3 == 0 or counter % 5 == 0:
                summation=summation+counter
        counter += 1
    #returns the sum
    return summation

# solves problem 2
def problem2():
    a = 1
    b = 1
    temp = 0
    summation = 0
    #finds the next fibonacci number
    #stops finding numbers when the next number is greater than 4000000
    while b <= 4000000:
        temp = b
        b = b + a
        a = temp
        #checks if the number is even and if so adds it to the sum
        if b % 2 == 0:
            summation = summation + b
    #returns the sum
    return summation

# the main part of the program
sol1 = problem1()
print "The sum of all the multiples of 3 or 5 below 1000 is {}".format(sol1)
sol2 = problem2()
print "The sum of the even-valued Fibonacci terms not exceeding four million is {}".format(sol2)
