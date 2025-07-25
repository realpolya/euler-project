'''
Totient Permutations

Euler's totient function, phi(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n 
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, phi(9)=6.

The number 1 is considered to be relatively prime to every positive number, 
so phi(1)=1. 
Interestingly, phi(87109)=79180, and it can be seen that 87109 is a 
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which 

1)phi(n) is a permutation of n and 
2)the ratio n/phi(n) produces a minimum.

'''

import math
from extras.utils import prime_factorization, sieve_eratosthenes

def is_permutation(num1, num2):
    '''compares whether two numbers are permutations of each other'''

    if num1 == num2:
        return False
    
    if len(str(num1)) != len(str(num2)):
        return False

    # see if lists are identical
    if sorted(list(str(num1))) == sorted(list(str(num2))):
        return True
    
    return False


def get_prime_factors(n, primes):
    '''non-recursive approach'''

    prime_factors = set()
    new_n = n

    for prime in primes:

        if prime > math.isqrt(n):
            break
        
        if new_n % prime == 0:

            prime_factors.add(prime)

            while new_n % prime == 0:
                new_n //= prime
    
    if new_n > 1:
        prime_factors.add(int(new_n))
    
    return prime_factors


def toti_perm(limit=100000):
    '''function adapted from problem 69'''

    min_toti = limit
    n_answer = 0
    mill_primes = sorted(sieve_eratosthenes(limit))

    sqrt_limit =  math.sqrt(limit)

    for i, prime in enumerate(mill_primes):

        if prime > sqrt_limit:
            break

        for prime_2 in mill_primes[i+1:]: # two distinct primes

            n = prime * prime_2

            if n > limit:
                break

            phi = n
            phi *= (1 - (1/prime))
            phi *= (1 - (1/prime_2))

            if phi.is_integer():
                phi = int(phi)
            else:
                continue

            ratio = n / phi

            if ratio < min_toti:

                # check if permutation
                if is_permutation(n, phi):

                    min_toti = ratio
                    n_answer = n

                    print("promising permutation found, n is ", n, "phi is", phi)


    return n_answer


print("Answer to problem 70: ", toti_perm(10**7))



# # OLD solution
# for n in range(2, limit+1):

#     # prime factors of n
#     n_primes = get_prime_factors(n, mill_primes)

#     if len(n_primes) > 2:
#         continue

#     phi = n

#     for prime in n_primes:

#         # totient formula
#         phi *= (1 - (1/prime))
    
#     if phi.is_integer():
#         phi = int(phi)
#     else:
#         continue
    
#     # if n == 87109:
#     #     print("phi is ", phi)
#     #     print("primes are", n_primes)

#     # calculate ratio
#     ratio = n / phi

#     if ratio < min_toti:

#         # check if permutation
#         if is_permutation(n, phi):

#             min_toti = ratio
#             n_answer = n

#             print("promising permutation found, n is ", n, "phi is", phi)
