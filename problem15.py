'''
Lattice Paths

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?

'''

import math

def find_routes(size):

    # implement binomial coefficient
    # n - total number of items
    # k - number of items to choose (number of decisions we have to make in order to arrive at the end point)

    n = size * 2
    k = size

    paths = int(math.factorial(n) / (math.factorial(k) ** 2))

    return paths

print(find_routes(4))

