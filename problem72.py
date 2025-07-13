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

# need to use Euler's totient function phi

from fractions import Fraction
from extras.utils import sieve_eratosthenes, is_relatively_prime, get_prime_factors

def counting_fractions(limit=8):
    '''Count reduced proper fractions below a limit'''

    primes = sieve_eratosthenes(limit)
    sorted_primes = sorted(primes)

    count = 0
    # dict = {}

    # for d in range(limit, 0, -1):

    #     dict[d] = get_prime_factors(d, sorted_primes)
    
    # print("dict done")

    # # i = 0
    # for d, d_set in dict.items():

    #     # co-primes would make a reduced fraction anyway
    #     coprimes = [n for n, n_set in dict.items() if n < d and d_set.isdisjoint(n_set)]
    #     count += len(coprimes)

    # totient sieve instead of dictionary
    phi = list(range(limit+1))
    # print(phi)

    for i in range(2, limit+1):

        # print("list is", phi, "i is", i)
        if phi[i] == i: # this would mean it is prime

            for j in range(i, limit + 1, i):

                phi[j] -= phi[j] // i

    count = sum(phi) - 1 # reduce by 1 to remove the 1/1

    return count

# print(counting_fractions())
print(counting_fractions(10**6))