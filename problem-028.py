problem = """
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# other than the center itself, the sum of diagonals for square at distance i from the center is
# 4(2i + 1)^2 - 2i - 4i - 6i = 16i^2 + 4i + 4
# sum of these sums = 16 sum i^2 + 4 sum i + 4 sum 1 = 16n(n+1)(2n+1)/6 + 4n(n+1)/2 + 4n
#   = 2n/3 (8n^2 + 15n + 13)
# then add 1 for the center
# for 1001 spiral, n = 500

n = 500
print 2*n * (8*n*n + 15*n + 13) / 3 + 1
