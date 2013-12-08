# coding: utf-8

problem = """
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

# t is triangle if there is some n >= 1 such that t = n(n+1)/2
# or equivalently, there is an integer solution to n^2 + n - 2t = 0
# the determinant is 1^2 - 4(1)(-2t) = 8t + 1, so if that is a perfect square then we're golden

from math import sqrt

def is_square(n):
    s = sqrt(n)
    return s == int(s)

def is_triangle(t):
    return is_square(8*t + 1)

def word_value(word):
    return sum([ord(ch) - ord('A') + 1 for ch in word])

# this function isn't needed for the problem but including it for fun
def triangle_numbers():
    t = 0
    d = 1
    while True:
        yield t
        t += d
        d += 1

with open('problem-042.txt') as fin:
    words = [quoted_word[1:-1] for quoted_word in fin.read().split(',')]
    triangle_words = [word for word in words if is_triangle(word_value(word))]
    print len(triangle_words)

    