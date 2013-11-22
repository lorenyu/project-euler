problem = """
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

primes = set()
composites = set()
for n in range(2, 1000000):
    if n in composites:
        continue
    primes.add(n)
    for m in range(2*n, 1000000, n):
        composites.add(m)

def is_circular(prime):
    global primes

    digits = str(prime)
    return all([int(digits[i:] + digits[:i]) in primes for i in range(len(digits))])

circular_primes = filter(is_circular, primes)

print len(circular_primes)
