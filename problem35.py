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

    # print(permutations)

    return permutations



def circular_primes(limit=100):

    circ_primes = []

    for n in range(1, limit):

        if is_prime(n):

            is_circular = True
            # print("n is ", n)
            # permutations = circ_permutate(list(str(n)))
            # print("permutations are", permutations)

            for permutation in circ_permutate(list(str(n))):

                if not is_prime(int(permutation)):
                    is_circular = False
                    break
            
            if is_circular:
                circ_primes.append(n)
    
    print(circ_primes)

    return len(circ_primes)


print(circular_primes(1000000))
# print(circular_primes(200))


# ---------------------------------------------------------------------------

# def permutate(array):
#     '''Recursive function to find all of the circular permutations of the set'''
#     print("array is ", array)

#     if len(array) == 1:
#         print("reached end of recursion, returning", array)
#         return array

#     permutations = []
#     first_element = array[0]
#     print("first element is ", first_element)
#     remaining = array[1:]
#     # print("remaining is ", remaining)

#     for p in permutate(remaining):

#         if not isinstance(p, list):
#             p = list(p)
#             print("ERROR: `p` is not a list. Value:", p)

#         for i in range(len(p) + 1):
#             # print("Slice before:", p[:i])
#             # print("First element to insert:", [first_element])
#             # print("Slice after:", p[i:])
#             print("adding now ", p[:i] + [first_element] + p[i:])
#             new_perm = p[:i] + [first_element] + p[i:]
#             print(new_perm)
#             permutations.append("".join(map(str, new_perm)))

#     print("permutations are ", permutations)
#     return permutations