'''
Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a 
prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most 
consecutive primes?

'''

from extras.utils import is_prime


def consecutive_prime_sum(limit=100):
    
    primes = [2]
    
    max_sum = 2 # answer
    current_sum = 2
    consecutive_primes = 0 # number of consecutive primes

    # cycle through numbers up to limit
    for n in range(3, limit, 2):

        # if prime, add to primes
        if is_prime(n):
            primes.add(n)

            # add to current sum
            current_sum += n

            # if sum is not prime, break the sequence ?
            if not is_prime(current_sum):
                current_sum = 0

            # if current_sum surpasses max_sum, reassign
            if current_sum > max_sum:

    
    return max_sum