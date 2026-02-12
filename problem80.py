'''
Square Root Digital Expansion

It is well known that if the square root of a 
natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., 
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital 
sums of the first one hundred decimal digits for all the irrational square roots.

'''

import math
from decimal import Decimal, getcontext, localcontext

def count_decimal_digits(num=2):

    # length of digits
    target_len = 99
    guard = 25
    work_precision = target_len + guard

    # assign length of digits to decimal
    # getcontext().prec = work_precision

    with localcontext() as ctx:

        ctx.prec = work_precision

        # sum = 0
        # complete = False

        n = Decimal(num)
        x = Decimal(1)

        while True:
            new_x = (x + (n / x)) / 2
            if x == new_x:
                break
            x = new_x
        
        # force fixed point output to see all of the digits
        fixed_point = format(x, 'f')
        int_part, frac_part = fixed_point.split('.', 1)
        zeros = "0" * target_len
        frac_part = (frac_part + zeros)[:target_len]

        frac_sum = sum(int(d) for d in frac_part)
        frac_sum += int(int_part)

        return frac_sum
    

def sum_decimal_digits_sqrt(num=2):

    target_len = 100
    scaled = math.isqrt(num * 10 ** (2 * target_len))

    s = str(scaled).zfill(target_len + 1)
    # frac = s[1:]
    first_100_digits = s[:target_len]
    frac_sum = sum(int(char) for char in first_100_digits)
    return frac_sum




print("for number 2, the count is: ", count_decimal_digits())
print("for number 2, the count of second function is: ", sum_decimal_digits_sqrt())