The Sieve of Eratosthenes is an ancient algorithm for finding prime numbers (a prime number is one that
is evenly divisible only by itself and 1). The algorithm works as follows:
To find all of the prime numbers between 1 and N (really 2 and N, since 1 is not considered a prime
number):

1. I list of the numbers between 2 and N. Initially, I will assume that all of them are prime. As
I decide that a number is not prime, we will cross it out.

2. For each un-crossed-out number:
2.1. I Initialize a new value to 2 times the current number. Cross out that number in the original list.
2.2. Repeat this crossing-out process for every multiple of the current number, up to and including
N.

3. At the end of the process, any numbers that have not been crossed out are prime.
To illustrate this process, consider the problem of identifying the prime numbers between 2 and 10:
Start by writing out the numbers under consideration:

2 3 4 5 6 7 8 9 10
2 is the next un-crossed out number. We need to cross out all of the multiples of 2 (4, 6, 8, and 10):
2 3 - 5 - 7 - 9 -
The next number is 3. We cross out its multiples, 6 (which was already crossed out) and 9:
2 3 - 5 - 7 - - -
The next remaining number is 5. Its only multiple is 10, which is already crossed out.
The last number left is 7, which has no multiples less than 10.
Thus, the prime numbers between 2 and 10 are 2, 3, 5, and 7.


-------------------------------------------------------------
A Wagstaff prime (named for mathematician Samuel S. Wagstaff, Jr.) is a prime number p of the form
p = (2q + 1) / 3
where q is a prime number greater than 2 (thus, the first Wagstaff prime starts with q == 3, and is (23 +
1) / 3 = 3).

Python function named wagstaff() that takes two arguments: a list of prime integers in
ascending order, and an integer value indicating how many Wagstaff primes should be generated. The
function does not return anything.
If the integer argument is greater than or equal to the size of the list, the function should print an error
message (to the effect that not enough prime numbers were supplied as input). Otherwise, it should print
a table with that many values of q and p, as in:
q (2^q + 1)/3
3 3
5 11
7 43
etc.
Use the list returned by your sieve() function as your source of prime integers.
