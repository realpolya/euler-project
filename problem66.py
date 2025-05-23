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

def find_next_convergent(D, triplet, first=False):

    start = math.sqrt(D)
    a0 = math.floor(start)
    # remainder = (start - a0).evalf()

    if first == True:
        next_step = a0
        remainder = (D - next_step * next_step)
    else:
        next_step = triplet.remainder * triplet.floor - triplet.next_step
        remainder = (D - next_step * next_step) // triplet.remainder
            
    floor = (a0 + next_step) // remainder

    return { next_step, floor, remainder}



    # # FIXME: the code below works for the convergents of e
    # if i % 3 == 2:
    #     a_series.append(2 * ((i + 1) // 3))
    # else:
    #     a_series.append(1)

    # # get the last member of a_series, the newest a
    # nested_fraction = Rational(a_series[-1])

    # # take the remaining a members from the series backwards
    # for a_num in reversed(a_series[:-1]):

    #     # adding current a to the the nested fraction
    #     nested_fraction = a_num + 1 / nested_fraction
    
    # convergent = simplify(a0 + 1 / nested_fraction)
    # print("convergent is ", convergent)

    # return digit_sum


def diophantine(limit):
    # TODO: need to calculate convergents, brute force does not work

    d_value = 0
    max_x = 0
    minimal_x = {}

    # loop
    for D in range(2, limit + 1):

        if math.sqrt(D).is_integer():
            continue

        x = 2

        # y = sqrt(x**2 - 1 / D)
        # y is always smaller than x
        # check if y is an integer
        not_an_integer = True

        while not_an_integer:

            # sum = x**2 - (D * y**2)
            y_squared = (x**2 - 1) / D
            y = math.sqrt(y_squared)
            print("y is ", y, "integer is ", y.is_integer(), "x is ", x, "D is ", D)

            if y.is_integer():

                minimal_x[D] = x

                if x > max_x:
                    max_x = x
                    d_value = D

                not_an_integer = False

            else:

                x += 1

    print(minimal_x)
    
    return d_value


print(diophantine(100))