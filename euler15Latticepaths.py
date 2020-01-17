# Lattice paths
# Called Central Binomial coefficient

from itertools import combinations
import math

def LatticePaths(n):
    #n is the grid size: nxn
    paths = math.factorial(2*n)/(math.factorial(n))**2
    return paths

final = LatticePaths(20)
print(final)