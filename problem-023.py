problem = """
A perfect number is a number for which the sum of its proper proper_divisors is exactly equal to the number. For example, the sum of the proper proper_divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper proper_divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt

def proper_divisors(n):
    if n == 1:
        return []
    result = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if n / i != i:
                result.append(n / i)
    return result

def abundant(n):
    return sum(proper_divisors(n)) > n

def sum_of_two_abundants(n):
    global sorted_abundants
    global abundants
    for i, a in enumerate(sorted_abundants):
        if a * 2 > n:
            break
        if n - a in abundants:
            return True
    return False

upper_bound = 28123
sorted_abundants = [i for i in range(1, upper_bound) if abundant(i)]
abundants = set(sorted_abundants)

print sum([i for i in range(1, upper_bound) if not sum_of_two_abundants(i)])
