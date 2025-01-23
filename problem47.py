'''
Distinct Primes Factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5.

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?

'''

from extras.utils import is_prime, prime_factorization

def distinct_factors(consecutive=2):

    primes = []
    winning_sequence = []
    sequence = 0
    n = 2

    while sequence < consecutive:
    
        if is_prime(n):
            primes.append(n)

        else:
            all_factors = []

            for prime in primes:
                all_factors = prime_factorization(n, prime) + all_factors
            
            print("for n", n, all_factors)

            if len(set(all_factors)) == consecutive: # need number of distinct factors
                
                if len(winning_sequence) == 0:
                    sequence += 1
                    winning_sequence.append(n)
                
                if len(winning_sequence) > 0:
                    if n - 1 == winning_sequence[-1]:
                        sequence += 1
                        winning_sequence.append(n)

            # lose a streak
            if sequence > 0 and len(set(all_factors)) != consecutive:

                sequence = 0
                winning_sequence.clear()

            if len(winning_sequence) > 0:
                
                if sequence > 0 and n - 1 != winning_sequence[-1]:
                    
                    sequence = 0
                    winning_sequence.clear()

        n += 1
    
    return winning_sequence
            

print(distinct_factors())



