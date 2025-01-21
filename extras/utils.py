import math

def is_prime(number):
    '''Check if the number is prime'''

    if number <= 1:
        return False 

    divisorFound = False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisorFound = True
            break

    if divisorFound:  
        # not a prime number
        return False

    return True


def is_pandigital(n, required_set):
    '''Check if the number is pandigital from 1 to n'''

    unique = set()
    not_pan = False
    string = str(n)

    for char in string:
        num = int(char)
        if num in unique or num == 0:
            not_pan = True
            return not not_pan
        unique.add(num)
    
    if unique != required_set:
        not_pan = True
    
    return not not_pan


def permutate(array):
    '''Find all of the permutations of the set'''

    if len(array) == 1:
        return str(array[0])

    permutations = []

    for n in range(len(array)):

        perm_start = array[n]
        remaining = array[:n] + array[n+1:]

        for p in permutate(remaining):

            string = "".join(str(perm_start) + str(p))
            permutations.append(string)

    return permutations


def is_pentagonal(num):
    '''is number pentagonal'''

    # quadratic formula
    n = (1 + math.sqrt(1 + (24 * num))) / 6

    if n.is_integer():
        return True
    
    return False


def is_hexagonal(num):
    '''is number hexagonal'''

    # 2n^2 - 1n - H
    n = (1 + math.sqrt(1 + (8 * num))) / 4

    if n.is_integer():
        return True
    
    return False