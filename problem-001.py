problem = """
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sumToN(n):
    """Returns sum of positive numbers less than or equal to n"""
    return n*(n+1)/2

def sumMultiplesToN(k, n):
    """Returns sum of positive multiples of k less than or equal to n"""
    return k*sumToN(int(n/k))

s3 = sumMultiplesToN(3, 999)
s5 = sumMultiplesToN(5, 999)
s15 = sumMultiplesToN(15, 999)
print s3 + s5 - s15
