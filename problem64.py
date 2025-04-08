'''
Odd Period Square Roots

'''

from fractions import Fraction
from sympy import sqrt, Rational, simplify # library for fractions
import math

# problem 26 also calculates infinite cycles
# only focus on irrational square roots

def odd_period_roots(limit=13):

    odd_count = 0

    for n in range(2, limit + 1):

        root = math.sqrt(n)

        if root.is_integer():
            continue
        
        period = []
        a0 = math.floor(root) # root = a0 + something < 1
        print(a0)

        step_one = a0 + sqrt(n) - a0
        # step_two = a0 + (1 / (1 / sqrt(n) - a0))
        intermediate_step = (1 / (sqrt(n) - a0)) * ((sqrt(n) + a0) / (sqrt(n) + a0))
        # denominator = (math.sqrt(n) - a0) * (math.sqrt(n) + a0)
        floor = math.floor(intermediate_step)
        print("for n ", n, "a1 is ", floor)

        # remainder = floor + 

        # create while block as we start calculating a1

        # the block will start repeating if the equation is the same

        # floor + remainder, floor + remainder, etc ....

        # 

    
odd_period_roots()