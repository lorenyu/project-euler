problem = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

N = 2000000
sum = 0
composites = [False]*N

i = 2
while i < N:
    sum += i
    n = 2*i
    while n < N:
        composites[n] = True
        n += i
    i += 1
    while i < N and composites[i]:
        i += 1
print sum
