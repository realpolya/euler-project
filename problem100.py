'''
Arranged Probability

If a box contains twenty-one coloured discs, composed of 
fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21) * 
(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance 
of taking two blue discs at random, is a box containing eighty-five blue 
discs and thirty-five red discs.

By finding the first arrangement to contain over 10^{12} = 1,000,000,000,000 
discs in total, determine the number of blue discs that the box would contain.

'''

# the solution is about generating the next one, not cycling over
# the numbers are too large to cycle over
# quadratic Diophantine equation

import math
from fractions import Fraction


def find_probability(b, total, repeat_times=2):

    probability = Fraction(b, total) * Fraction(b - 1, total - 1)

    return probability


# print("15/21 = ", Fraction(15, 21), "and 14/20 = ", Fraction(14, 20))
# print("85/120 = ", Fraction(85, 120), "and 84/119 = ", Fraction(84, 119))
# print(Fraction(5, 7) * Fraction(7, 10))
# print(Fraction(17, 24) * Fraction(12, 17))
# print(float(find_probability(85, 120)))

# one of the numerators and denominators have to be the same number

# def diopantine_equation():

#     Fraction(b, total) * Fraction(b - 1, total - 1) = 1/2

def arranged_probability():

    # unknown number of reds, unknown number of blues

    # find first instance first

    # nested loops of blue and red, until the answer is found

    answer = False
    # blue = 500000000000
    blue = 10

    while not answer:

        for red in range (int(0.3 * blue), int(0.5 * blue)):

            # print("blue", blue, "red", red)

            total_quantity = red + blue
            probability = find_probability(blue, total_quantity)

            # probability = Decimal(find_probability(blue, total_quantity))
            # rounded_p = probability.quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN)

            if float(probability) == 0.5:
                print("blue are ", blue)
                print("B/N = ", Fraction(blue, total_quantity), "and B-1/N-1 = ", Fraction(blue - 1, total_quantity - 1))

                # answer = blue
                # print("blue discs:", blue, "red discs:", red, "total: ", total_quantity, "probability is ", probability)
                # print("ratio of blue to total quantity is ", round(blue / total_quantity, 5))

            
            # elif probability < 0.5: # means that red already grew too much

            #     break

        if blue == 100000:
            answer = True
        
        blue += 1
    
    return answer

print(arranged_probability())


''' 
blue are  15
B/N =  5/7 and B-1/N-1 =  7/10
blue are  85
B/N =  17/24 and B-1/N-1 =  12/17
blue are  493
B/N =  29/41 and B-1/N-1 =  41/58
blue are  2871
B/N =  99/140 and B-1/N-1 =  70/99
blue are  16731
B/N =  169/239 and B-1/N-1 =  239/338



12, 12, 70, 70

17, 17, 99, 99

5, 29, 29, 169

7, 41, 41, 99


'''