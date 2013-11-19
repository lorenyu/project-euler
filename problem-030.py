problem = """
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

digits = [0,1,2,3,4,5,6,7,8,9]
power = 5

def num(digits):
    return sum([digit*(10**i) for i, digit in enumerate(digits)])

def sum_of_powers_of_digits(digits, power):
    return int(sum([digit**power for digit in digits]))

found = set()
stack = [[]]
while True:
    if len(stack) <= 0:
        break
    cur_digits = stack.pop()
    s = sum_of_powers_of_digits(cur_digits, power)
    n = num(cur_digits)
    if n == s:
        found.add(n)
    if n + 10**len(cur_digits) > s + 9**power:
        continue
    for digit in digits:
        stack.append(cur_digits + [digit])

found = [num for num in found if len(str(num)) > 1]
print sum(found)

