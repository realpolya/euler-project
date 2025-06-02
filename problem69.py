'''
Totient Maximum

Euler's totient function, phi(n) [sometimes called the phi function], 
is defined as the number of positive integers not exceeding n which 
are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than or equal to nine and relatively prime to nine, 
phi(9)=6.

It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.
Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

'''

import math
from extras.utils import prime_factorization, sieve_eratosthenes

# find a number of positive integers below n
# that are relatively prime to n

# def find_divisors(n):

#     divisors = set()
#     more_divisors = set()
#     # divisors.add(1)

#     for num in range(2, math.floor(math.sqrt(n))+1):

#         if n % num == 0:
#             divisors.add(num)
    
#     for num in divisors:

#         more_divisors.add(n / num)

#     divisors.add(n)
#     divisors.update(more_divisors)

#     return divisors


def totient_max(limit=10):

    max_toti = 0
    max_n = 0
    mill_primes_unsorted = sieve_eratosthenes(1000000)
    mill_primes = sorted(mill_primes_unsorted)

    for n in range(2, limit+1):

        # print("starting with n ", n)
        # prime_count = 1 # number 1 is already included

        # n_divisors = find_divisors(n)
        # print("divisors of n are ", n_divisors)
        # relative_primes = set()
        # relative_primes.add(1)

        n_primes = []

        for prime in mill_primes:

            # print("prime is ", prime, "n is ", n)

            if prime > math.sqrt(n):
                break

            n_primes = prime_factorization(n, prime) + n_primes

        n_prime_set = set(n_primes)
        # n_primes = prime_factorization(n)

        phi = n

        for prime in n_prime_set:

            # totient formula
            phi *= (1 - (1/prime))


        # for candidate in range(2, n):




        #     if candidate % 2 == 0 and 2 in n_divisors:
        #         continue

        #     coprime = True

        #     # if is_relatively_prime(n, candidate):
        #     # print("for n ", n, "testing candidate", candidate)

        #     for num in range(2, candidate + 1):

        #         # print("candidate is ", candidate, "divided by ", num, "remainder is ", candidate % num)

        #         if candidate % num == 0 and num in n_divisors:
        #             # print("candidate is out: ", candidate, "it is divisible by ", num, "which is in n_divisors", n_divisors)
        #             coprime = False
        #             break
        
        #     if coprime:
        #         # print("coprime found")
        #         prime_count += 1
        #         # relative_primes.add(candidate)
            
        # ratio = n / prime_count
        ratio = n / phi

        # print("for n ", n, "coprimes are ", relative_primes)

        if ratio > max_toti:
            max_toti = ratio
            max_n = n

    print("max toti is ", max_toti, "max n is", max_n)

    return max_n
    
totient_max(1000000)




















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