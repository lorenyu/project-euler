problem = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?
"""

from math import sqrt

numPrimes = 10001
primes = []

def isPrime(n):
    global primes
    for i in range(0, len(primes)):
        if n % primes[i] == 0:
            return False
    return True

n = 2
for i in range(0,numPrimes):
    while not isPrime(n):
        n += 1
    primes.append(n)

print primes[numPrimes-1]
