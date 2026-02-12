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

from decimal import Decimal, getcontext

def count_decimal_digits(num=2):

    # length of digits
    target_len = 100

    # assign length of digits to decimal
    getcontext().prec = target_len

    sum = 0
    complete = False

    x = Decimal(1)
    n = Decimal(num)

    count = 0

    # need to increase resolution

    # use the Newton-Raphson formula for computing digits
    while not complete:

        # use x 
        new_x = (x + (n / x)) / 2

        print("new_x is ", new_x, "old x is", x)

        # reassign x
        x = new_x

        decimals = str(new_x).split(".", 1)[1]

        if len(decimals) >= target_len:

            for d in decimals:

                sum += int(d)

            complete = True
        
        count += 1

        # 10 rounds for now
        if count > 10:

            complete = True
    
    return sum



print(count_decimal_digits())

# def is_num_irrational(num=2):

