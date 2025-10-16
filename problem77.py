'''
Prime Summations

It is possible to write ten as the sum of primes in exactly five 
different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes 
in over five thousand different ways? (5000 ways)

'''

from extras.utils import sieve_eratosthenes

# number of ways to sum up to the composite number
LIMIT = 5

# limit of sieve of eratosthenes
PRIME_LIMIT = 20


def prime_partitions(limit=LIMIT, prime_limit=PRIME_LIMIT):

    # up to which number?
    primes = sorted(sieve_eratosthenes(prime_limit))

    # dynamic programming list
    dp_list = [0] * (prime_limit + 1)
    dp_list[0] = 1

    for p in primes:
        for i in range(p, limit + 1):
            dp_list[i] += dp_list[i - p]

    print(dp_list)

prime_partitions()