'''
Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and 
concatenating them in any order the result will always be prime. For example, taking 7 and 109, 
both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for 
a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

from extras.utils import is_prime

# find the lowest sum of the five primes for which any two primes concatenate to produce another prime


def is_concat_prime(num_1, num_2):

    # try concatenating combinations within that set
    concat_1 = int(str(num_1) + str(num_2))
    concat_2 = int(str(num_2) + str(num_1))

    if not is_prime(concat_1) and not is_prime(concat_2):
        return False
    
    return True


def prime_pair_sets(quantity=4):

    lowest_sum = 0
    limit = 1000
    primes = [2]

    # create a set of primes up to a certain number
    for i in range(3, limit, +2):
        if is_prime(i):
            primes.append(i)
    
    pairs = []

    # while loop
    while lowest_sum == 0:

        # work in pairs?
        for prime in primes:
            for prime_2 in primes:

                # if a combination is not prime, discard that pair
                if not is_concat_prime(prime, prime_2):
                    continue

                pairs.append([prime, prime_2])

                # if a second pair is not working with first, find another larger pair

                # keep track of pairs

                # if for loops fail, increase the primes set

                # if pairs are found, assign the lowest sum
        
        lowest_sum = 2
    
    print(len(pairs))

prime_pair_sets()