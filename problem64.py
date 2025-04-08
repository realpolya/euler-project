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
        next_steps = set()
        a0 = math.floor(root) # root = a0 + something < 1
        print(a0)

        period_not_done = True
        current_a = a0

        while period_not_done:

            step_one = current_a + sqrt(n) - current_a
            next_step = (sqrt(n) + current_a) / (n - (current_a ** 2))

            if next_step in next_steps:
                period_not_done = False

                if len(period) % 2 != 0:
                    odd_count += 1


            else:
                next_steps.add(next_step)

                floor = math.floor(next_step)
                print("for n ", n, "a1 is ", floor)

                period.append(floor)

            current_a = floor

        # remainder = floor + 

        # create while block as we start calculating a1

        # the block will start repeating if the equation is the same

        # floor + remainder, floor + remainder, etc ....

    
odd_period_roots()