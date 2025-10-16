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
LIMIT = 5000

# limit of sieve of eratosthenes
PRIME_LIMIT = 100

def prime_partitions(limit=LIMIT, prime_limit=PRIME_LIMIT):

    # up to which number?
    primes = sorted(sieve_eratosthenes(prime_limit))

    answer = None

    # dynamic programming list
    dp_list = [0] * (prime_limit + 1)
    dp_list[0] = 1

    for p in primes:
        for i in range(p, prime_limit + 1):
            dp_list[i] += dp_list[i - p]

    for i, dp in enumerate(dp_list):
        if dp >= limit:
            answer = i
            break

    # print("for number", answer-1, "the number of prime summations is", dp_list[answer-1])
    # print("for number", answer, "the number of prime summations is", dp_list[answer])

    return answer

print("Answer to problem 77: ", prime_partitions())