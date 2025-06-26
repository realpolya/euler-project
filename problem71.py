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
from extras.utils import sieve_eratosthenes, get_prime_factors
import time

def is_relatively_prime(num1, num2, primes):
    '''check if 2 numbers are co-prime'''

    # calculate divisors for each n
    for n in primes:

        if num1 % n == 0 and num2 % n == 0:
            return False
        
        if n > num1:
            return True




# an irreducible fraction if HCF is 1
# find a fraction smaller than 3 / 7 (numerator)

def ordered_fractions(limit=8):

    primes = sieve_eratosthenes(limit)

    fractions = set()
    target = Fraction(3, 7)
    prev_target = Fraction(2, 5)

    for d in range(1, limit+1):

        # d_factors = get_prime_factors(d, primes)
        n_max = int(d * target) + 1
        n_min = int(d * prev_target)

        for n in range(n_min, n_max):

            # if n in d_factors:
            #     continue
            
            if Fraction(n, d) < prev_target:
                continue

            if Fraction(n, d) > target:
                break

            if Fraction(n, d) in fractions:
                continue
            
            # n_factors = get_prime_factors(n, primes)

            # if not d_factors.isdisjoint(n_factors):
            #     continue
            
            if is_relatively_prime(n, d, primes):
                fractions.add(Fraction(n, d))
        

    # # n and d

    # # get a set or a list of irreducible fractions below the limit

    # # for each d, run through n up to d (nested loops - won't work as it is too large)
    # for d in range(1, limit+1):

    #     for n in range(1, d):

    #         if is_relatively_prime(n, d):

    #             fractions.append(Fraction(n, d))
    

    sorted_fractions = sorted(fractions)

    # print(sorted_fractions)

    # # locate 3/7
    answer_i = 0
    for i, fraction in enumerate(sorted_fractions):

        if fraction == target:
            answer_i = i - 1
        
    # # find numerator
    return sorted_fractions[answer_i]
            

print(ordered_fractions(10000))


# 3/7 is close to half, need to look at numbers in 
# that area (n should be half of d)
# look for numbers between 2/5 and 3/7
# instead of looping, GENERATE fractions?

#is relatively prime very inefficient