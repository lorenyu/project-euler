problem = """
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindromic(s):
    return s[:len(s)/2] == s[:(len(s)-1)/2:-1]

def decimal2binary(num):
    x = ''
    while num > 0:
        x = str(num % 2) + x
        num /= 2
    return x

double_base_palindromes = set()

for num in range(1000):
    p1 = int(str(num) + str(num)[-2::-1])
    p2 = int(str(num) + str(num)[::-1])
    if is_palindromic(decimal2binary(p1)):
        double_base_palindromes.add(p1)
    if is_palindromic(decimal2binary(p2)):
        double_base_palindromes.add(p2)

print sum(double_base_palindromes)
