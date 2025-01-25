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
    found = False

    for n in range(1000, 9999):

        if is_prime(n):

            n_permutations = [int(n) for n in permutate(list(str(n)))]
            prime_perms = []
            counter = 0

            if 1487 in set(n_permutations):
                continue

            for perm in set(n_permutations):

                if is_prime(perm) and len(str(perm)) > 3:

                    prime_perms.append(perm)
                    counter += 1

            if counter < 2:

                continue
            
            prime_perms.sort()
        
            differences = []
            repeating_diff = []

            for i, prime in enumerate(prime_perms):

                remaining = prime_perms[i+1:]

                for second_prime in remaining:

                    difference = abs(prime - second_prime)

                    if difference in differences:
                        repeating_diff.append(difference)

                    if difference != 0:
                        differences.append(difference)
            

            for num in sorted(repeating_diff):

                twice = num * 2

                for prime in prime_perms:

                    if (prime + twice) in prime_perms and (prime + num) in prime_perms:

                        found = True
                        final_sequence += str(prime)
                        final_sequence += str(prime + num)
                        final_sequence += str(prime + twice)
                
        if found:

            break

    
    return final_sequence


print("Answer to problem 49: ",find_permutations())