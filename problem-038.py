# coding: utf-8

problem = """
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer k with (1,2, ... , n) where n > 1?
"""

from itertools import permutations, imap

def concatentated_product(k):
    result = ''
    n = 1
    while True:
        if len(result) >= 9:
            break
        result += str(k * n)
        n += 1
    return result

def can_be_formed_as_concatenated_product(num):
    for num_digits in range(1,5):
        k = int(num[:num_digits])
        if num == concatentated_product(k):
            return True
    return False

for num in imap(''.join, permutations('987654321')):
    if can_be_formed_as_concatenated_product(num):
        print num
        break
