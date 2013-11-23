problem = """
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from itertools import count

right_truncatable_primes_by_num_digits = {
    1: set([2,3,5,7])
}
left_truncatable_primes_by_num_digits = {
    1: set([2,3,5,7])
}
primes = set()
composites = set()
truncatable_primes = set()

for n in count(2):
    num_digits = len(str(n))

    if num_digits > 6: # this part is hardcoded =( not sure how to mathematically prove that this is the upper bound
        break

    if num_digits > 2 and not right_truncatable_primes_by_num_digits.has_key(num_digits - 1) and left_truncatable_primes_by_num_digits.has_key(num_digits - 1):
        break

    # compute primes

    if n in composites:
        continue

    primes.add(n)
    for m in range(2*n,1000000,n): # this part is hardcoded =( not sure how to mathematically prove that this is the upper bound
        composites.add(m)

    # add to truncatable primes

    if num_digits <= 1:
        continue

    left_truncatable_primes = left_truncatable_primes_by_num_digits.setdefault(num_digits, set())
    right_truncatable_primes = right_truncatable_primes_by_num_digits.setdefault(num_digits, set())

    if int(str(n)[1:]) in left_truncatable_primes_by_num_digits[num_digits-1]:
        left_truncatable_primes.add(n)

    if int(str(n)[:-1]) in right_truncatable_primes_by_num_digits[num_digits-1]:
        right_truncatable_primes.add(n)

    if n in left_truncatable_primes and n in right_truncatable_primes:
        truncatable_primes.add(n)

print sum(truncatable_primes)
