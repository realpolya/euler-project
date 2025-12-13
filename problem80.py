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

def count_decimal_digits(num=2):

    target_len = 100
    sum = 0
    complete = False
    x = 1

    count = 0

    # use the Newton-Raphson formula
    while not complete:

        # use x 
        new_x = (1 / 2) * (x + (num / x))

        print("new_x is ", new_x, "old x is", x)

        # reassign x
        x = new_x


        decimals = str(new_x).split(".", 1)[1]

        if len(decimals) >= target_len:

            for d in decimals:

                sum += int(d)

            complete = True
        
        count += 1

        if count > 10:

            complete = True
    
    return sum



print(count_decimal_digits())

# def is_num_irrational(num=2):

