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

    # for n in range(2, limit + 1):

    n = 23

    root = math.sqrt(n)

    # if root.is_integer():
    #     continue
    
    period = []
    next_steps = set()
    a0 = math.floor(root) # root = a0 + something < 1
    # print(a0)

    period_not_done = True
    current_a = a0
    increment = 1

    while period_not_done:

        # step_one = current_a + sqrt(n) - current_a

        if increment == 1:
            denominator = n - (current_a ** 2)
            next_step = (sqrt(n) + current_a) / denominator
        else:
            next_step = simplify(1 / remainder)
            # print("new remainder is ", new_remainder)
            # next_step = 
        
        floor = math.floor(next_step)

        # what is left after the next_step? the remainder?
        remainder = simplify(next_step - floor)

        # print("next step is ", simplify(next_step))
        # print("remainder is ", remainder)

        if next_step in next_steps:
            period_not_done = False
            print("period is ", period)

            if len(period) % 2 != 0:
                odd_count += 1
        else:
            next_steps.add(next_step)

            
            # print("for n ", n, "a", increment, " is ", floor)

            period.append(floor)

        current_a = floor
        increment += 1

        # remainder = floor + 

        # create while block as we start calculating a1

        # the block will start repeating if the equation is the same

        # floor + remainder, floor + remainder, etc ....
    
    return odd_count

    
print("odd count is: ", odd_period_roots())