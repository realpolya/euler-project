'''
Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and 
concatenating them in any order the result will always be prime. For example, taking 7 and 109, 
both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for 
a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

import math
import time

from extras.utils import is_prime

def find_candidates(member_1, member_2, sets_1, sets_2, dict, limit, candidates=None):
    '''Recursive function that calculates candidates to be concatenated into primes'''

    if candidates is None:
        candidates = []

    # base case
    if limit == 0:
        return candidates
    
    current_members = {member_1, member_2}
    new_candidates = [num for num in sets_1 if num in sets_2 and num not in current_members]

    if len(new_candidates) == 0:
        return []
    
    for candidate in new_candidates[:]:

        new_set = dict[candidate]
        next_candidates = find_candidates(member_1, candidate, new_candidates, new_set, dict, limit - 1, new_candidates)
        
        if not next_candidates:
            new_candidates.remove(candidate)

    return new_candidates


def is_concat_prime(num_1, num_2, primes):
    '''concatenates two numbers to see if all concatenations yield primes'''

    concat_1 = int(str(num_1) + str(num_2))
    concat_2 = int(str(num_2) + str(num_1))

    if concat_1 not in primes or concat_2 not in primes:
        return False
    
    return True


def sieve_eratosthenes(limit):
    '''calculates a set of primes up to a limit'''

    is_prime_cache = [True] * limit # Sieve of Eratosthenes
    is_prime_cache[0] = is_prime_cache[1] = False # 0 and 1 are not primes

    for num in range(2, math.isqrt(limit) + 1):
        if is_prime_cache[num]:
            for multiplied in range(num ** 2, limit, +num):
                is_prime_cache[multiplied] = False
    
    prime_set = {num for num, prime in enumerate(is_prime_cache) if prime}

    return prime_set


def prime_pair_sets():
    '''finds the lowest sum for the set of 5 concatenating primes'''

    start_time = time.time()

    lowest_sum = 0
    limit = 100000
    large_limit = 10**8

    primes = sorted(sieve_eratosthenes(limit))
    large_prime_set = sieve_eratosthenes(large_limit)

    print(f"1. Execution time: {time.time() - start_time:.2f} seconds")
    start_time = time.time()

    pairs = set()
    pairs_dict = {p: set() for p in primes}

    for i, prime in enumerate(primes):

        for prime_2 in primes[i+1:]:

            new_pair = (prime, prime_2)
            if new_pair not in pairs:

                if not is_concat_prime(prime, prime_2, large_prime_set):
                    continue

                pairs_dict[prime].add(prime_2)
                pairs_dict[prime_2].add(prime)
                pairs.add(new_pair)
    
    print(f"2. Execution time: {time.time() - start_time:.2f} seconds")
    start_time = time.time()

    four_subsets_dict = {p: candidates for p, candidates in pairs_dict.items() if len(candidates) >= 4}
    valid_keys = set(four_subsets_dict.keys())
    four_subsets_dict = {p: {v for v in values if v in valid_keys} for p, values in four_subsets_dict.items()}  

    four_subset_pairs = []

    for pair in pairs:
        member_1, member_2 = pair

        if member_1 in four_subsets_dict and member_2 in four_subsets_dict:
            if pair not in four_subset_pairs:
                four_subset_pairs.append(pair)


    print(f"3. Execution time: {time.time() - start_time:.2f} seconds")
    start_time = time.time()
    
    for pair in four_subset_pairs:

        member_1, member_2 = tuple(pair)

        member_1_subsets = four_subsets_dict[member_1]
        member_2_subsets = four_subsets_dict[member_2]

        candidates = find_candidates(member_1, member_2, member_1_subsets, member_2_subsets, four_subsets_dict, 3)
        if candidates:
            print("for member_1", member_1, "and member_2", member_2, "candidates are", candidates)
            lowest_sum = sum(candidates) + member_1 + member_2
            break
    
    print(f"4. Execution time: {time.time() - start_time:.2f} seconds")

    return lowest_sum


print("Answer to problem 60: ", prime_pair_sets())