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

def diophantine(limit):

    d_value = 0
    max_x = 0
    minimal_x = {}

    # loop
    for D in range(2, limit + 1):

        if math.sqrt(D).is_integer():
            continue

        # sum = 0
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


            # if sum == 1 and x > max_x:

            #     max_x = x
            #     d_value = D
            
            # elif sum != 1:

            #     x += 1

    print(minimal_x)
    
    return d_value

print(diophantine(7))