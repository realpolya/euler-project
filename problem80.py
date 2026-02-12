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

from decimal import Decimal, getcontext, localcontext

def count_decimal_digits(num=2):

    # length of digits
    target_len = 100
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
        frac_part = fixed_point.split('.', 1)[1]
        zeros = "0" * target_len
        frac_part = (frac_part + zeros)[:target_len]

        frac_sum = sum(int(d) for d in frac_part)
        return frac_sum

        # count = 0

        # # need to increase resolution

        # # use the Newton-Raphson formula for computing digits
        # while not complete:

        #     # use x 
        #     new_x = (x + (n / x)) / 2

        #     # if the two are the same, the precision stays the same
        #     if x == new_x:

        #         complete = True

        #     print("new_x is ", new_x, "old x is", x)

        #     # reassign x
        #     x = new_x

        #     # change to fixed-point formatting
        #     decimals = str(new_x).split(".", 1)[1]

        #     if len(decimals) >= target_len:

        #         for d in decimals:

        #             sum += int(d)

        #         complete = True
            
        #     count += 1

        #     # 10 rounds for now
        #     if count > 10:

        #         complete = True
    
    # return sum

print(count_decimal_digits())