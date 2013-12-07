# coding: utf-8

problem = """
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

# 1-9 (9), 10-99 (90), 100-999 (900), 1000-9999 (9000)

from itertools import count

def d(n):
    n -= 1 # go from 1-based indexing to 0-based indexing for convenience
    m = 0
    for k in count():
        num_digits = k + 1
        span = (9 * 10**k) * num_digits
        i = n - m
        if i <= span:
            num = 10**k + (i / num_digits)
            return int(str(num)[i % num_digits])
        m += span

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
