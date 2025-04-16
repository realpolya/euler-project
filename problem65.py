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
    remainder = E - a0
    prev_term = Rational(0)
    a_series = []

    for _ in range(limit):

        current_x = 1 / remainder
        current_a = math.floor(current_x)
        a_series.append(current_a)
        print("current a is ", current_a)
        remainder = current_x - current_a

        print("prev_term is ", prev_term)
        new_term = simplify(1 / (current_a + prev_term))
        prev_term = new_term

        print("terms so far:", a0, "and series are ", a_series)
        result = simplify(a0 + new_term)


        print(result)
    


find_convergents()