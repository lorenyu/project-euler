problem = """
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations, imap
from math import sqrt

primes = set()
composites = set([1])

upper_bound = int(sqrt(987654321))
for i in range(2, upper_bound+1):
    if i in composites:
        continue
    primes.add(i)
    for j in range(2*i, upper_bound+1, i):
        composites.add(j)

def is_prime(p):
    if p <= 1:
        return False
    if p in primes:
        return True
    for d in primes:
        if d > p:
            break
        if p % d == 0:
            return False
    return True

def pandigital_primes():
    for n in range(9, 1, -1):
        for p in imap(lambda p: int(''.join(map(str, p))), permutations(range(n,0,-1))):
            if is_prime(p):
                yield p

print next(pandigital_primes())
