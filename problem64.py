'''
Odd Period Square Roots

'''

from fractions import Fraction
import math

# problem 26 also calculates infinite cycles

# only focus on irrational square roots

def odd_period_roots(limit=13):

    for n in range(2, limit + 1):

        root = math.sqrt(n)

        if root.is_integer():
            continue
        
        a0 = math.floor(root)
        print(a0)
    
odd_period_roots()