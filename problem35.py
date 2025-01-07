'''
Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

import math
from collections import deque
from extras.utils import is_prime


def circ_permutate(array):

    permutations = []

    # establish number of permutations
    perm_num = len(array)
    copied = deque(array) # from collections

    for _ in range(perm_num):   

        # add permutation
        permutations.append("".join(map(str, copied)))
        copied.rotate(1)

    return permutations



def circular_primes(limit=100):

    circ_primes = []

    for n in range(1, limit):

        if is_prime(n):

            is_circular = True

            for permutation in circ_permutate(list(str(n))):

                if not is_prime(int(permutation)):
                    is_circular = False
                    break
            
            if is_circular:
                circ_primes.append(n)
    
    print(circ_primes)

    return len(circ_primes)

print("Answer to problem 35: ", circular_primes(1000000))