problem = """
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial
from itertools import takewhile, count, combinations_with_replacement, imap

def largest_sum(num_digits):
    return largest_sum.f * num_digits
largest_sum.f = factorial(9)

def smallest_num(num_digits):
    return 10**(num_digits - 1)

max_num_digits = max(takewhile(lambda num_digits: largest_sum(num_digits) >= smallest_num(num_digits), count(1)))

numbers = set()

base_digits = [0,1,2,3,4,5,6,7,8,9]
for num_digits in range(1, max_num_digits+1):
    for x in combinations_with_replacement(zip(base_digits, map(factorial, base_digits)), num_digits):
        digits, digit_factorials = zip(*x)
        if len(digits) < 2:
            continue
        number = sum(digit_factorials)
        if (tuple(map(int, sorted(str(number)))) == digits):
            numbers.add(number)

print sum(numbers)
