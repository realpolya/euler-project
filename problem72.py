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
from extras.utils import sieve_eratosthenes, is_relatively_prime, get_prime_factors

def counting_fractions(limit=8):
    '''Count reduced proper fractions below a limit'''

    primes = sieve_eratosthenes(limit)
    sorted_primes = sorted(primes)

    count = 0
    # fractions = []

    # the roughest version is to create nested loops – but it can't work
    # for limit such as 10**6
    # for d in range(2, limit+1):

    #     for n in range(1, d):

    #         if is_relatively_prime(n, d, primes):

    #             count += 1
    #             print("count is ", count)
    #             # fractions.append(Fraction(n, d))
    
    # print(fractions)

    # for each d generate a list of numbers list_n 
    # that are co-prime to d
    # and less than d

    dict = {}

    # print(get_prime_factors(100, sorted_primes))

    for d in range(limit, 0, -1):

        dict[d] = get_prime_factors(d, sorted_primes)
    
    print("dict done")

    # i = 0
    for d, d_set in dict.items():

        # co-primes would make a reduced fraction anyway
        coprimes = [n for n, n_set in dict.items() if n < d and d_set.isdisjoint(n_set)]

        count += len(coprimes)

        # print("d is ", d, "factors are ", factors_set)
        # i += 1


    return count

print(counting_fractions())
# print(counting_fractions(10**6))