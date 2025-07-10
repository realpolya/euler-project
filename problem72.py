'''
Counting Fractions

Consider the fraction,  n / d, where n and d are positive integers.
If n < d and HCF(n,d)=1, it is called a reduced 
proper fraction.

If we list the set of reduced proper fractions for d <= 8 in 
ascending order of size, we get:

1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 2 / 7, 
1 / 3, 3 / 8, 2 / 5, 3 / 7, 1 / 2, 4 / 7, 
3 / 5, 5 / 8, 2 / 3, 5 / 7, 3 / 4, 4 / 5, 
5 / 6, 6 / 7, 7 / 8

It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper 
fractions for d <= 1,000,000?

'''

from fractions import Fraction
from extras.utils import sieve_eratosthenes, is_relatively_prime

def counting_fractions(limit=8):
    '''Cound reduced proper fractions below a limit'''

    primes = sieve_eratosthenes(limit)

    count = 0

    # the roughest version is to create nested loops – but it can't work
    # for limit such as 10**6

    

