problem = """
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):
    """Returns whether n is a palindromic number."""
    s = str(n)
    for i in range(0, len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

pMax = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        if isPalindrome(p) and p > pMax:
            pMax = p

print pMax
