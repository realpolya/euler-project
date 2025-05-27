'''
Convergents of e


Find sum of digits in the numerator of the 100th convergent of the continued 
fraction for e.

'''

import math
from sympy import simplify, Rational, E

def find_convergents(limit=10):

    start = E
    a0 = math.floor(E)
    remainder = (E - a0).evalf()
    count = 1
    a_series = []


    for i in range(1, limit + 1):

        if i % 3 == 2:
            a_series.append(2 * ((i + 1) // 3))
        else:
            a_series.append(1)

        # get the last member of a_series, the newest a
        nested_fraction = Rational(a_series[-1])

        # take the remaining a members from the series backwards
        for a_num in reversed(a_series[:-1]):

            # adding current a to the the nested fraction
            nested_fraction = a_num + 1 / nested_fraction
        
        convergent = simplify(a0 + 1 / nested_fraction)
        count += 1

        if count == limit:
            numerator, denominator = convergent.as_numer_denom()
            numerator_answer = numerator
            break

    digit_sum = 0
    for char in list(str(numerator_answer)):
        digit_sum += int(char)


    return digit_sum


print("Answer to problem 65: ", find_convergents(100))