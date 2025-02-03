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


differences in numerators and denominators
12, 12, 70, 70
17, 17, 99, 99

5, 29, 29, 169
7, 41, 41, 239

sequence = 

B / N
numerators
B1num + B2 - 1num = B2num
B2num + B2 - 1num = B3num
B3num + B4 - 1num = B4num
B4num + B4 - 1num = B5num

denominators
N1den + N2 - 1den = N2den
N2den + N2 - 1den = N3den
N3den + N4 - 1den = N4den
N4den + N4 - 1den = N5den

B - 1 / N - 1
numerators
B1 - 1num + B1num = B2 - 1num
B2 - 1num + B3num = B3 - 1num
B3 - 1num + B3num = B4 - 1num
B4 - 1num + B5num = B5 - 1num

denominators
N1 - 1den + N1den = N2 - 1den
N2 - 1num + N3num = N3 - 1num
N3 - 1num + N3num = N4 - 1num
N4 - 1num + N5num = N5 - 1num


'''

def number_of_blues(frac_b, frac_n, frac_bs, frac_ns):
    '''get two fractions, find the smallest integer values of B and N'''
    # B = frac_b * k
    # N = frac_n * k

    # B - 1 = frac_bs * m
    # N - 1 = frac_ns * m

    # k = (frac_bs * m + 1) / frac_b
    # k = (frac_ns * m + 1) / frac_n

    # frac_b * (frac_ns * m + 1) = (frac_bs * m + 1) * frac_n
    # frac_b * frac_ns * m + frac_b = frac_bs * m * frac_n + frac_n
    # frac_b * frac_ns * m - frac_bs * m * frac_n = frac_n - frac_b
    # m = (frac_n - frac_b) / (frac_b * frac_ns - frac_bs * frac_n)

    m = (frac_n - frac_b) / (frac_b * frac_ns - frac_bs * frac_n)
    k = (frac_bs * m + 1) / frac_b

    B = frac_b * k
    N = frac_n * k

    Bs = frac_bs * m
    Ns = frac_ns * m

    print("B/N", B, "/", N)
    print("B-1/N-1", Bs, "/", Ns)

    if N > 1000000000000:
        return B

    return False



def create_sequence(b1, n1, b1s, n1s, limit): #s for smaller

    b_list = [b1]
    n_list = [n1]
    bs_list = [b1s, b1 + b1s]
    ns_list = [n1s, n1 + n1s]

    alternate = True
    counter = 0
    i = 0

    while i < limit:

        if alternate:

            if counter == 0:

                # print("b list is ", b_list, "index is ", i)
                next_b = b_list[i] + bs_list[i+1]
                b_list.append(next_b)
                next_n = n_list[i] + ns_list[i+1]
                n_list.append(next_n)
                counter += 1
            
            elif counter == 1:

                next_b = b_list[i] + bs_list[i]
                b_list.append(next_b)
                next_n = n_list[i] + ns_list[i]
                n_list.append(next_n)
                counter = 0

                alternate = False

        else:
            
            if counter == 0:

                next_bs = b_list[i] + bs_list[i-1]
                bs_list.append(next_bs)
                next_ns = n_list[i] + ns_list[i-1]
                ns_list.append(next_ns)
                counter += 1
            
            elif counter == 1:

                i -= 2
                next_bs = b_list[i+1] + bs_list[i+1]
                bs_list.append(next_bs)
                next_ns = n_list[i+1] + ns_list[i+1]
                ns_list.append(next_ns)
                counter = 0

                alternate = True
        
        i += 1
    
    sequence = []
    sequence_s = []

    for i in range(len(b_list)):
        sequence.append(Fraction(b_list[i], n_list[i]))

    for i in range(len(bs_list)):
        sequence_s.append(Fraction(bs_list[i], ns_list[i]))
    
    if len(b_list) > len(bs_list):
        length = len(bs_list)
    else:
        length = len(b_list)

    for i in range(length):
        B = number_of_blues(b_list[i], n_list[i], bs_list[i], ns_list[i])
        if B:
            return B
    
    return False
    
    # print("b/n sequence")
    # for frac in sequence:
    #     print(frac)
    
    # print("b-1/n-1 sequence")
    # for frac in sequence_s:
    #     print(frac)


def arranged_probability():

    answer = False
    i = 2

    while not answer:
        answer = create_sequence(5, 7, 7, 10, i)
        i += 1
    
    return answer

print(int(arranged_probability()))











# def find_probability(b, total, repeat_times=2):

#     probability = Fraction(b, total) * Fraction(b - 1, total - 1)

#     return probability


# # print("15/21 = ", Fraction(15, 21), "and 14/20 = ", Fraction(14, 20))
# # print("85/120 = ", Fraction(85, 120), "and 84/119 = ", Fraction(84, 119))
# # print(Fraction(5, 7) * Fraction(7, 10))
# # print(Fraction(17, 24) * Fraction(12, 17))
# # print(float(find_probability(85, 120)))

# # one of the numerators and denominators have to be the same number

# # def diopantine_equation():

# #     Fraction(b, total) * Fraction(b - 1, total - 1) = 1/2

# def arranged_probability():

#     # unknown number of reds, unknown number of blues

#     # find first instance first

#     # nested loops of blue and red, until the answer is found

#     answer = False
#     # blue = 500000000000
#     blue = 10

#     while not answer:

#         for red in range (int(0.3 * blue), int(0.5 * blue)):

#             # print("blue", blue, "red", red)

#             total_quantity = red + blue
#             probability = find_probability(blue, total_quantity)

#             # probability = Decimal(find_probability(blue, total_quantity))
#             # rounded_p = probability.quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN)

#             if float(probability) == 0.5:
#                 print("blue are ", blue)
#                 print("B/N = ", Fraction(blue, total_quantity), "and B-1/N-1 = ", Fraction(blue - 1, total_quantity - 1))

#                 # answer = blue
#                 # print("blue discs:", blue, "red discs:", red, "total: ", total_quantity, "probability is ", probability)
#                 # print("ratio of blue to total quantity is ", round(blue / total_quantity, 5))

            
#             # elif probability < 0.5: # means that red already grew too much

#             #     break

#         if blue == 100000:
#             answer = True
        
#         blue += 1
    
#     return answer

# # print(arranged_probability())