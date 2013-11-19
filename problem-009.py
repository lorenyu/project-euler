problem = """
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# since 3c > a + b + c = 1000, c > 1000/3
# since 2b^2 > a^2 + b^2 = c^2, b > c/sqrt(2)
# substituting c = 1000 - (a + b) into a^2 + b^2 = c^2, we get
# a = (1,000b - 500,000) / (b - 1,000)
# since 3a < a + b + c = 1000, a < 1000/3, which implies (1,000b - 500,000) / (b - 1,000) < 1000/3
# solving for b, and noting that b - 1000 is a negative number, we get
# b > 250
# since b < 1000 - c, 1000 - c must be at least 250, so c is at most 750

from math import sqrt, ceil

for c in range(250,750):
    for b in range(ceil(c / sqrt(2)), 1000 - c):
        a = (1000.0*b - 500000.0) / (b - 1000.0)
        if a > 0 and a + b + c == 1000:
            print int(a*b*c)
