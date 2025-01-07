'''
Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

import math
from extras.utils import is_prime

def permutate(array):
    '''Recursive function to find all of the circular permutations of the set'''
    # print("array is ", array)

    if len(array) == 1:
        return [array]

    permutations = []
    first_element = array[0]
    remaining = array[1:]
    # print("remaining is ", remaining)

    for p in permutate(remaining):

        if not isinstance(p, list):
            # print("ERROR: `p` is not a list. Value:", p)
            p = list(p)

        for i in range(len(p) + 1):
            # print("Slice before:", p[:i])
            # print("First element to insert:", [first_element])
            # print("Slice after:", p[i:])
            new_perm = p[:i] + [first_element] + p[i:]
            print(new_perm)
            permutations.append("".join(map(str, new_perm)))

    print("permutations are ", permutations)
    return permutations



def circular_primes(limit=100):

    circ_primes = []

    for n in range(195, limit):

        if is_prime(n):

            is_circular = True
            print("n is ", n)

            for permutation in permutate(list(str(n))):

                if not is_prime(int(permutation)):
                    print("permutation", permutation, "is not prime")
                    is_circular = False
                    break
            
            if is_circular:
                circ_primes.append(n)
    
    print(circ_primes)

    return len(circ_primes)


# print(circular_primes(1000000))
print(circular_primes(200))
