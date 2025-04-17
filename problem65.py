'''
Convergents of e


Find sum of digits in the numerator of the 100th convergent of the continued 
fraction for e.

'''

import math
from sympy import simplify, Rational, E

def find_convergents(limit=3):

    # write function for the square root of 2

    # a0 = math.floor(math.sqrt(2))
    # prev_term = Rational(0)

    # for _ in range(10):

    #     new_term = simplify(1 / (2 + prev_term))
    #     prev_term = new_term

    #     result = simplify(a0 + new_term)

    #     print(result)
    
    a0 = math.floor(E)
    remainder = (E - a0).evalf()
    print("remainder is ", remainder)
    prev_term = Rational(0)
    a_series = []

    for _ in range(limit):

        something = simplify(1 / (1 / remainder))

        current_x = 1 / remainder
        a = math.floor(current_x)
        remainder = simplify(current_x - a)

        # add to a series
        a_series.append(a)

        # print("prev_term is ", prev_term) # FIXME: prev_term is an issue

        # simple_r = simplify(1 / (1 / math.floor(remainder)))
        simple_r = simplify(1 / math.floor(remainder))

        new_term = simplify(1 / a) # remainder instead of prev_term
        # prev_term = new_term

        print("terms so far:", a0, "and series are ", a_series)
        result = simplify(a0 + (1 / new_term))


        print(result)

    start = math.sqrt(2)
    a0 = math.floor(math.sqrt(2))

    r = start - a0
    print(r)
    print(math.floor(1 / r))
    a1 = math.floor(1 / r)

    convergent = a0 + 1 / math.floor(1 / r)
    print("convergent is ", convergent)

    new_r = simplify((1 / r) - a1)
    a2 = math.floor(1 / new_r)

    convergent = a0 + 1 / (a1 + 1 / math.floor(1 / new_r))
    print("convergent is ", convergent)

    very_new_r = simplify((1 / new_r) - a2)
    a3 = math.floor(1 / very_new_r)

    convergent = a0 + 1 / (a1 + 1 / (a2 + 1 / math.floor(1 / very_new_r)))
    print("convergent is ", convergent)







    


find_convergents()