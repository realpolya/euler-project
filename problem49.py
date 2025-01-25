'''
Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in 
which each of the terms increases by 3330, is unusual in 
two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, 
or 3-digit primes, exhibiting this property, but there is one 
other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the 
three terms in this sequence?

'''

from extras.utils import is_prime, permutate

def find_permutations():

    final_sequence = ""

    for n in range(1000, 9999):

        if is_prime(n):

            # check if there are at least two other 
            # prime permutations
            # in the set

            n_permutations = permutate(list(str(n)))
            prime_perms = [n]
            counter = 0

            for perm in n_permutations:

                if is_prime(perm):

                    prime_perms.append(perm)
                    counter += 1
            
            if counter < 2:

                continue
            
            prime_perms.sort()

            if 



