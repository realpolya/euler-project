'''
Odd Period Square Roots

'''

from fractions import Fraction
# from sympy import sqrt, Rational, simplify # library for fractions
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
        triplets = set()
        a0 = math.floor(root) # root = a0 + something < 1

        period_not_done = True
        current_a = a0
        increment = 1

        while period_not_done:

            if increment == 1:
                next_step = (math.sqrt(n) + current_a) / (n - (current_a ** 2))
            else:
                next_step = 1 / remainder
                # next_step = 1 / remainder
            
            floor = math.floor(next_step)

            # what is left after the next_step? the remainder?
            remainder = next_step - floor
            # remainder = next_step - floor

            # print("next step is ", simplify(next_step))
            # print("remainder is ", remainder)

            triplet = [next_step, floor, remainder]

            if triplet in triplets:
                period_not_done = False

                if len(period) % 2 != 0:
                    print("for n", n, "period is ", period)
                    odd_count += 1
            else:
                triplets.add(triplet)
                # print("for n ", n, "a", increment, " is ", floor)
                period.append(floor)

            current_a = floor
            increment += 1
    

    return odd_count

    
print("odd count is: ", odd_period_roots(10000))