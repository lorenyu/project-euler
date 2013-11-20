problem = """
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# Observations:
# The product cannot have three or fewer digits (the smallest product containing six digits is 11111 x 1 = 11111, which is greater than any three digit number)
# Also, the product cannot have five or more digits (the largest product containing four digits is 99 x 99 = 9801, which is smaller than any five digit number)
# Thus, the product must have four digits.

from itertools import permutations, combinations, product as iproduct, imap

digits = set([1,2,3,4,5,6,7,8,9])

def digits2num(digits):
    return reduce(lambda x, d: x*10 + d, digits)

def num2digits(num):
    return set(map(int, str(num)))

pandigital_products = set()
for operand_digits in imap(set, combinations(digits, 5)):
    for num_multiplicand_digits in range(3,4+1):
        for multiplicand_digits in imap(set, combinations(operand_digits, num_multiplicand_digits)):
            multiplier_digits = operand_digits - multiplicand_digits
            for multiplicand, multiplier in iproduct(imap(digits2num, permutations(multiplicand_digits)), imap(digits2num, permutations(multiplier_digits))):
                product = multiplicand * multiplier
                product_digits = num2digits(product)
                if len(str(product)) + len(operand_digits) == 9 and 0 not in product_digits and len(product_digits | operand_digits) == 9:
                    pandigital_products.add(product)

print sum(pandigital_products)