problem = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    m = max(a, b)
    n = min(a, b)
    while True:
        q = m / n
        r = m % n
        if r == 0:
            return n
        m = n
        n = r

def lcm(a, b):
    """Returns the least common multiple of a and b."""
    return a * b / gcd(a, b)

def gcdList(nums):
    """Returns the greatest common divisor of a list of numbers."""
    d = nums[0]
    for n in nums[1:]:
        d = gcd(d, n)
    return d

def lcmList(nums):
    m = nums[0]
    for n in nums[1:]:
        m = lcm(m, n)
    return m

nums = range(1, 21)
print lcmList(nums)
