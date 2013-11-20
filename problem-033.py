problem = """
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from itertools import product
from fractions import gcd

def digits(num):
    return set(map(int, str(num)))

fractions = []
for n, d in product(range(10, 100), range(10, 100)):
    if n > d:
        continue
    n_digits = digits(n)
    d_digits = digits(d)
    if len(n_digits) < 2:
        continue
    if len(d_digits) < 2:
        continue
    if n % 10 == 0 and d % 10 == 0:
        continue
    common_digits = n_digits & d_digits
    if len(common_digits) != 1:
        continue
    n2 = tuple(n_digits - common_digits)[0]
    d2 = tuple(d_digits - common_digits)[0]
    if n * d2 == n2 * d:
        fractions.append((n,d))

n, d = reduce(lambda (xn, xd), (n, d): (xn * n, xd * d), fractions, (1, 1))
print d / gcd(n, d)
