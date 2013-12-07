# coding: utf-8

problem = """
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

def solutions(p):
    for a in range(1, int(p/(2 + sqrt(2)))+1):
        b = float(p)*a/(p - a)
        if b != int(b):
            continue
        b = int(b)
        c = p - a - b
        yield a, b, c

def num_solutions(p):
    return len([s for s in solutions(p)])

print max(range(1000+1), key=num_solutions)
