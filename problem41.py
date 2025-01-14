'''
Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

from extras.utils import is_prime, permutate


def find_max_prime_in_perm(perms):

    max_prime = 0

    for perm in perms:
        if is_prime(int(perm)) and int(perm) > max_prime:
            max_prime = int(perm)
    
    if max_prime != 0:
        return max_prime
    
    return False


def pandigital_prime():

    max_prime = False
    required_set = []

    for n in range(1, 10):
        required_set.append(n)
    
    for n in range (9, 0, -1):
        max_prime = find_max_prime_in_perm(permutate(required_set))

        if max_prime:
            break
        
        required_set.pop()

    return max_prime


print("Answer to problem 41: ", pandigital_prime())