'''
Odd Period Square Roots

'''

import math

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
                next_step = a0
                remainder = (n - next_step * next_step)
            else:
                next_step = remainder * floor - next_step
                remainder = (n - next_step * next_step) // remainder
            
            floor = (a0 + next_step) // remainder

            triplet = (next_step, floor, remainder)

            if triplet in triplets:
                period_not_done = False

                if len(period) % 2 != 0:
                    odd_count += 1

            else:
                triplets.add(triplet)
                period.append(floor)

            current_a = floor
            increment += 1
    
    return odd_count

    
print("Answer to problem 64: ", odd_period_roots(10000))