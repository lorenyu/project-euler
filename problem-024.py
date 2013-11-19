problem = """
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = 1000000-1
remaining_digits = [0,1,2,3,4,5,6,7,8,9]
digits = []
while n > 0:
    f = factorial(len(remaining_digits)-1)
    i = int(n / f)
    digit = remaining_digits[i]
    n -= i * f
    digits.append(digit)
    remaining_digits.remove(digit)
digits.extend(remaining_digits)
print ''.join([str(digit) for digit in digits])