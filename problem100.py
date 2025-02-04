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

import math
from fractions import Fraction


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

    if N > 1000000000000:
        return B

    return False



def create_sequence(b1, n1, b1s, n1s): #s for smaller

    b_list = [b1]
    n_list = [n1]
    bs_list = [b1s, b1 + b1s]
    ns_list = [n1s, n1 + n1s]
    B = False

    alternate = True
    counter = 0
    i = 0

    while not B:

        if alternate:

            if counter == 0:

                # print("b list is ", b_list, "index is ", i)
                next_b = b_list[i] + bs_list[i+1]
                b_list.append(next_b)
                next_n = n_list[i] + ns_list[i+1]
                n_list.append(next_n)

                B = number_of_blues(b_list[i+1], n_list[i+1], bs_list[i+1], ns_list[i+1])

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

                B = number_of_blues(b_list[i], n_list[i], bs_list[i], ns_list[i])

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

    return B




def arranged_probability():

    answer = int(create_sequence(5, 7, 7, 10))

    return answer



print("Answer to problem 100: ", arranged_probability())





'''

Solution observations:

# the solution is about generating the next one, not cycling over
# the numbers are too large to cycle over
# quadratic Diophantine equation

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
