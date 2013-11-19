problem = """
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def lengthOf(n):
    if n == 1:
        return 1
    if n < maxN and sequenceLength[n] != 0:
        return sequenceLength[n]
    if n % 2 == 0:
        result = lengthOf(n / 2) + 1
    else:
        result = lengthOf(3*n + 1) + 1

    if n < maxN:
        sequenceLength[n] = result
    return result

maxN = 1000000
sequenceLength = [0]*maxN
maxLen = 0
maxStartingNum = 0
for i in range(1,maxN):
    length = lengthOf(i)
    if length > maxLen:
        maxLen = length
        maxStartingNum = i
print maxStartingNum
