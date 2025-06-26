'''
Ordered Fractions

Consider the fraction,  n / d, where n and d are positive integers. 
If n < d and HCF(n,d)=1, it is called a reduced proper 
fraction.

If we list the set of reduced proper fractions for d < 8 in ascending 
order of size, we get:

1 / 8,  1 / 7,  1 / 6,  1 / 5,  1 / 4,  2 / 7,  1 / 3,  3 / 8,  2 / 5,  3 / 7,
1 / 2,  4 / 7,  3 / 5,  5 / 8,  2 / 3,  5 / 7,  3 / 4,  4 / 5,  5 / 6,  6 / 7,  7 / 8

It can be seen that  2 / 5 is the fraction immediately 
to the left of  3 / 7.

By listing the set of reduced proper fractions for d <= 1,000,000 
in ascending order of size, find the numerator of the fraction immediately 
to the left of  3 / 7.


'''

from fractions import Fraction

def is_relatively_prime(num1, num2):
    '''check if 2 numbers are co-prime'''

    # divisors1 = set()
    # divisors2 = set()

    max_num = 0

    if num1 > num2:
        max_num = num1
    elif num2 > num1 or num1 == num2:
        max_num = num2

    # must not have common divisors greater than 1

    # calculate divisors for each n
    for n in range(2, max_num):

        if num1 % n == 0 and num2 % n == 0:
            return False
        
        if n > num1 or n > num2:
            break

        # divisor_true = [False, False]

        # if num1 % n == 0:
        #     # divisors1.add(n)
        #     divisor_true[0] = True
        
        # if num2 % n == 0:
        #     # divisors2.add(n)
        #     divisor_true[1] = True
        
        # if all(divisor_true):
        #     return False

    # is there overlap?
    return True




# an irreducible fraction if HCF is 1
# find a fraction smaller than 3 / 7 (numerator)

def ordered_fractions(limit=8):

    fractions = []

    # n and d

    # get a set or a list of irreducible fractions below the limit

    # for each d, run through n up to d (nested loops - won't work as it is too large)
    for d in range(1, limit+1):

        for n in range(1, d):

            if is_relatively_prime(n, d):

                fractions.append(Fraction(n, d))
    

    fractions.sort()

    print(fractions)
            



    # find numerator

ordered_fractions()

