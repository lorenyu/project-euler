problem = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

num = 600851475143
largestPrimeFactor = 2

def largestPrimeFactor(n):
    """Returns the largest prime factor of n."""
    if n == 1:
        return None
    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            return max(largestPrimeFactor(m), largestPrimeFactor(n/m))
        m -= 1
    return n

print largestPrimeFactor(600851475143)
