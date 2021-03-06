problem = """
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumOfSquares(n):
    """Returns sum_i=[1:n] i^2."""
    return n*(n+1)*(2*n+1)/6

def sumToN(n):
    """Returns sum_i=[1:n] i."""
    return n*(n+1)/2

n = 100
s = sumToN(n)
squareOfSums = s**2
print squareOfSums-sumOfSquares(n)
