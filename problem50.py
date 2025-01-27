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

    max_sum = 0 # answer
    max_cons_primes = 0

    for n in range(3, limit, +2):

        # if prime, add to primes
        if is_prime(n):

            primes.append(n)
    

    for i, prime in enumerate(primes):

        current_sum = prime
        chain_length = 1

        for prime_two in primes[i+1:]:

            current_sum += prime_two
            chain_length += 1 # counter increases even if the intermediate step is not a prime

            if current_sum > limit:
                break

            if is_prime(current_sum) and chain_length > max_cons_primes:
                max_cons_primes = chain_length
                max_sum = current_sum


    return max_sum

print("Answer to problem 50: ", consecutive_prime_sum(1000000))