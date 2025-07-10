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
from extras.utils import sieve_eratosthenes, get_prime_factors, is_relatively_prime


def ordered_fractions(limit=8):

    primes = sieve_eratosthenes(limit)

    target = Fraction(3, 7)
    prev_target = Fraction(2, 5)
    answer = prev_target

    start_n = int(target * limit)
    start_d = int(start_n * (1 / target))

    while Fraction(start_n, start_d) > prev_target:
        start_d -= 1
        start_n -= 1

    # for d in range(1, limit+1):
    for d in range(start_d, limit+1):

        # calculate n instead of looping
        n = int(d * target)

        if is_relatively_prime(n, d, primes):
            if Fraction(n, d) > answer and Fraction(n, d) < target:
                answer = Fraction(n, d)
        
    return answer.numerator
            

print("Answer to problem 71: ", ordered_fractions(10**6))