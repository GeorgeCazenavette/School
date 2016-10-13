###########################################################################################
# Name: George Cazenavette
# Date: 2/3/2016
# Description: Project Euler 5-8
###########################################################################################

# it may help to make use of some math functions (which you can import)
# it may also help to define other "helper" functions (i.e., delegate tasks!)
import time
import math

# I decided to make this fuction robust so I could use it in future assigments
def isPrime(n):
    #checks if the number is 1 (not prime)
    if n == 1:
        return False
    #checks if the number is 2 or 3 (prime)
    elif (n == 2 or n == 3):
        return True
    #checks if the number is even (prime)
    elif (n % 2 == 0):
        return False
    #checks if the number is less than 9 (all the non primes have already been taken care of)
    elif (n < 9):
        return True
    #checks if the number is divisible by 3 (not prime)
    elif (n % 3 == 0):
        return False
    else:
        #sets the upper limit for potential factors to the sqareroot of the candidate
        y = math.sqrt(n)
        x = 5
        #only checks factors until the upper limit is reached
        while (x <= y):
            if (n % x == 0):
                return False
            if (n % (x + 2) == 0):
                return False
            #skips multiples of 3 since those were already checked
            x += 6
        return True


# solves problem 5
#I made this to work with any number, not just 20.
def problem5():
	# write your code below for this problem (and remove this comment...)
    primes = []
    #the largest number for which we are looking for a least common multiple
    x = 20
    n = 1
    #creates a list of the prime numbers less or equal to than x
    while (n <= x):
        if isPrime(n):
            primes.append(n)
        n += 1

    #creates a parallel list of zeros for the list of primes
    count = [0] * len(primes)
    
    #only have to check 11-20 sese they are multiples of 1-10
    for i in range(11, 20):
        #checks the dividend against the list of primes
        for j in range(0, len(primes)):
            counter = 0
            a = i
            b = primes[j]
            #increments the counter for evertime the dividend is divisible by the prime
            while (a % b == 0):
                counter += 1
                a /= b
            #replaces the current max of that prime if the current is larger
            if (counter > count[j]):
                count[j] = counter
    multiple = 1
    #multiplies the prime factorizations of the numbers together, minus duplicate factors
    for k in range(0, len(primes)):
        multiple = multiple * (primes[k] ** count[k])
    return multiple
        
    
# solves problem 6
def problem6():
	# write your code below for this problem (and remove this comment...)
    sum1 = 0
    sum2 = 0
    #increments through the first 100 natural numbers
    for i in range (1, 101):
        #keeps a sum of the numbers
        sum1 += i
        #keeps a sum of the numbers squared
        sum2 += i ** 2
    #returns the square of sum minus the sum of squares
    return sum1 ** 2 - sum2
    
# solves problem 7
def problem7():
	# write your code below for this problem (and remove this comment...)
    #keeps track of the number of primes
    #starts at 1 because the counter skips 2
    n = 1
    #counts up from 1
    number = 1
    while (n < 10001):
        number += 2
        if isPrime(number):
            #increments the number of primes
            n += 1
    #returns the number when the 1000th prime is found
    return number
    
# solves problem 8
def problem8():
	# write your code below for this problem (and remove this comment...)
    #a string of the big number
    grid = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    #variable for the largest found product
    num = 0
    #these loops cycle through every possible combination of 13 adjacent digits
    for i in range(0, len(grid) - 13):
        #keeps track of the temporary product for each itteration
        prod = 1
        for j in range(i, i + 13):
            #when j is finished iterating, prod will be the product of the 13 adjacent digits
            prod = prod * int(grid[j])
        #replaces the largest product found if the current product is bigger
        if (prod > num):
            num = prod
    return num
# the main part of the program

#t=time.time()
sol5 = problem5()
#runtime=time.time()-t
print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(sol5)
#print "runtime="+str(runtime)
#t=time.time()
sol6 = problem6()
#runtime=time.time()-t
print "The difference between the sum of squares and square of sum of the first 100 natural numbers is {}".format(sol6)
#print "runtime="+str(runtime)
#t=time.time()
sol7 = problem7()
#runtime=time.time()-t
print "The 10,001st prime number is {}".format(sol7)
#print "runtime="+str(runtime)
#t=time.time()
sol8 = problem8()
#runtime=time.time()-t
print "The greatest product of thirteen adjacent digits is {}".format(sol8)
#print "runtime="+str(runtime)
