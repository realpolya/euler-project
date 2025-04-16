'''
Convergents of e


Find sum of digits in the numerator of the 100th convergent of the continued 
fraction for e.

'''

import math
from sympy import simplify, Rational

def find_convergents():

    # write function for the square root of 2

    a0 = math.floor(math.sqrt(2))
    prev_term = Rational(0)

    for _ in range(10):

        new_term = simplify(1 / (2 + prev_term))
        prev_term = new_term

        result = simplify(a0 + new_term)

        print(result)
    
find_convergents()




