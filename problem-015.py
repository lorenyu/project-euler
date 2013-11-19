problem = """
Starting in the top left corner of a 2*2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20*20 grid?
"""

# let x_m,n be the number of routes for an mxn grid.
# then x_(m,n) = 1 if either n or m == 0
#            = x_(m-1,n) + x_(m,n-1) otherwise
#
# basically you end up with Pascal's numbers

from numpy import *

(m,n) = (20,20)
x = zeros((m+1,n+1), long)
for i in range(0,m+1):
    x[i,0] = 1
for j in range(0,n+1):
    x[0,j] = 1
for i in range(1,m+1):
    for j in range(1,n+1):
        x[i,j] = x[i-1,j] + x[i,j-1]
print x[m,n]
