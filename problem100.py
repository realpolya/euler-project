'''
Arranged Probability

If a box contains twenty-one coloured discs, composed of 
fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21) * (14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance 
of taking two blue discs at random, is a box containing eighty-five blue 
discs and thirty-five red discs.

By finding the first arrangement to contain over 10^{12} = 1,000,000,000,000 
discs in total, determine the number of blue discs that the box would contain.

'''

# 0.33, 0.4, 0.411

import math
from decimal import Decimal, ROUND_HALF_EVEN

def find_probability(item_quantity, total_quantity, repeat_times=2):

    probability = 1

    for _ in range(repeat_times):

        # print(item_quantity, total_quantity)
        probability *= item_quantity / total_quantity
        item_quantity -= 1
        total_quantity -= 1


    return probability

# print(find_probability(85, 120))

def arranged_probability():

    # unknown number of reds, unknown number of blues

    # find first instance first

    # nested loops of blue and red, until the answer is found

    answer = False
    blue = 500000000000

    while not answer:

        for red in range (int(0.33 * blue), blue):

            total_quantity = red + blue
            probability = find_probability(blue, total_quantity)

            # probability = Decimal(find_probability(blue, total_quantity))
            # rounded_p = probability.quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN)

            if math.isclose(probability, 0.5, rel_tol=1e-9):

                answer = blue
                print("blue discs:", blue, "red discs:", red, "total: ", total_quantity, "probability is ", probability)
            
            # elif probability < 0.5: # means that red already grew too much

            #     break
        
        blue += 1
    
    return answer

print(arranged_probability())