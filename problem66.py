'''
Diophantine Equation

Consider quadratic Diophantine equations of the form:
x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, 
the largest x is obtained when D=5.
Find the value of D <= 1000 in minimal solutions of x 
for which the largest value of x is obtained.

'''

import math
from sympy import Rational, simplify


def find_next_convergent(D, a0, first=False, triplet=None):
    '''Find the next convergent in the continued fractions series'''

    if first == True:
        next_step = a0
        remainder = (D - next_step * next_step)
    else:
        next_step = triplet["remainder"] * triplet["floor"] - triplet["next_step"]
        remainder = (D - next_step * next_step) // triplet["remainder"]
            
    floor = (a0 + next_step) // remainder

    obj = { 
        "next_step": next_step, 
        "floor": floor, 
        "remainder": remainder
    }
    
    return obj


def diophantine(limit):

    d_value = 0
    max_x = 0
    minimal_x = {}

    for D in range(2, limit + 1):

        if math.sqrt(D).is_integer():
            continue
        
        # generate convergents such as x / y = sqrt(D)
        # test the convergent in the equation
        # stop when convergent satisfies the equation wiht integers

        not_found = True
        first = True
        a_series = []
        start = math.sqrt(D)
        a0 = math.floor(start)

        while not_found:

            if first:
                new_triplet = find_next_convergent(D, a0, True)
                first = False
            else:
                prev_triplet = new_triplet.copy() # create a copy
                new_triplet = find_next_convergent(D, a0, False, prev_triplet)
            
            # add new floor to the series
            a_series.append(new_triplet["floor"])

            # get the last member of a_series, the newest a
            nested_fraction = Rational(a_series[-1])

            # take the remaining a members from the series backwards
            for a_num in reversed(a_series[:-1]):

                # adding current a to the the nested fraction
                nested_fraction = a_num + 1 / nested_fraction
            
            convergent = simplify(a0 + 1 / nested_fraction)

            # see if the convergent works (x is numerator, y is denominator)
            x, y = convergent.as_numer_denom()

            # check the equation
            if x**2 - D * y**2 == 1:

                if x > max_x:
                    max_x = x
                    d_value = D

                not_found = False
    
    return d_value


print("Answer to problem 66: ", diophantine(1000))