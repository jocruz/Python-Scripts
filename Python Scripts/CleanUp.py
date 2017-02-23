import math

def fac(n):
    if (n <= 1): #This is the base case
        return 1 #Return one for all other cases in which n is lower than 1
    else:
        return n * fac(n-1) # You multiply n by the last input of n

print (fac(3)) #Test run case

# 3 *  (factorial (2))
# factorial (2) == 2 * (factorial (1))
#factorial (1) == 1
# 3 * 2 * 1
# Answer comes out to 6
