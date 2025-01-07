'''
Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

from extras.utils import is_prime

def permutate(array):
    '''Find all of the permutations of the set'''

    if len(array) == 1:
        return str(array[0])

    permutations = []
    answer = False

    # number of permutations equals to factorial of length
    perm_num = math.factorial(len(array))

    for n in range(len(array)):

        perm_start = array[n]

        remaining = array[:n] + array[n+1:]

        for p in permutate(remaining):

            string = "".join(str(perm_start) + str(p))
            permutations.append(string)

    return permutations



def circular_primes(limit=100):

    circ_primes = []

    for n in range(1, limit):

        if is_prime(n):

            is_curious = True

            for permutation in permutate(list(str(n))):

                if not is_prime(permutation):
                    is_curious = False
                    break
            
            if is_curious:
                circ_primes.append(n)
    
    return len(circ_primes)


print(circular_primes())
