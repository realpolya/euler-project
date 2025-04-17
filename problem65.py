'''
Convergents of e


Find sum of digits in the numerator of the 100th convergent of the continued 
fraction for e.

'''

import math
from sympy import simplify, Rational, E

def find_convergents(limit=10):

    # write function for the square root of 2

    # a0 = math.floor(math.sqrt(2))
    # prev_term = Rational(0)

    # for _ in range(10):

    #     new_term = simplify(1 / (2 + prev_term))
    #     prev_term = new_term

    #     result = simplify(a0 + new_term)

    #     print(result)
    
    start = E
    a0 = math.floor(E)
    remainder = (E - a0).evalf()
    # print("remainder is ", remainder)
    prev_term = Rational(0)
    prev_a = 0
    count = 1

    a_series = []
    # for i in range(1, limit):
    #     if i % 3 == 2:
    #         a_series.append(2 * ((i + 1) // 3))
    #     else:
    #         a_series.append(1)


    for i in range(1, limit + 1):

        # a = math.floor(1 / remainder)
        # prev_r = remainder
        # remainder = simplify((1 / prev_r) - a)

        # # add to a series
        # a_series.append(a)

        # result = a0

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

        # print("terms so far:", a0, "and series are ", a_series)

        # print("convergent is ", convergent)
        count += 1
        print("convergent number ", count, "convergent is ", convergent)

        if count == limit:
            print("length: ", len(a_series))
            numerator, denominator = convergent.as_numer_denom()
            numerator_answer = numerator
            # print("for count ", count, "numerator is ", numerator)
            break
            
        
    # s = "6992432529593258630263690665699787787145693139"
    # print("here we go ", sum(int(c) for c in s))  # should print 258

    digit_sum = 0
    for char in list(str(numerator_answer)):
        digit_sum += int(char)
        # print("added ", int(char), ". now sum is ", digit_sum)

    print("a series is ", a_series)
    print("numerator is ", numerator_answer)

    return digit_sum

    # start = math.sqrt(2)
    # a0 = math.floor(math.sqrt(2))

    # r = start - a0
    # print(r)
    # print(math.floor(1 / r))
    # a1 = math.floor(1 / r)

    # convergent = a0 + 1 / math.floor(1 / r)
    # print("convergent is ", convergent)

    # new_r = simplify((1 / r) - a1)
    # a2 = math.floor(1 / new_r)

    # convergent = a0 + 1 / (a1 + 1 / math.floor(1 / new_r))
    # print("convergent is ", convergent)

    # very_new_r = simplify((1 / new_r) - a2)
    # a3 = math.floor(1 / very_new_r)

    # convergent = a0 + 1 / (a1 + 1 / (a2 + 1 / math.floor(1 / very_new_r)))
    # print("convergent is ", convergent)







    


print(find_convergents(100))