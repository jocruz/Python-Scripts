

def sieve (n):
    candidates = [1] * (n+1)
    
    for i in range(2, n+1):
        if candidates[i] == 1:
            # Mark off all multiples of i as non-prime
            for v in range(i*2, n+1, i):
                candidates[v] = 0
    
    # Create a new, primes-only list
    primes = []
    for x in range(2, n+1):
        if candidates[x] == 1:
            primes.append(x)
    
    return primes


def wagstaff (primes, n):
    if n >= len(primes):
        print "Insufficient data to generate that many Wagstaff primes!"
    else:
        print "q\t(2^q + 1)/3"
        
        for i in range(1,n+1):
            q = primes[i]
            wag = (2**q + 1)/3
            print q, "\t", wag


max = int(raw_input("Please enter the maximum value to consider: "))
p = sieve(max)
print
print "The prime numbers from 2 through", max,"are:", p
print
n = int(raw_input("How many Wagstaff primes would you like to generate? "))
print
wagstaff(p, n)
