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


def sieve_eratosthenes(limit):
    '''Calculate a set of primes up to a limit'''

    is_prime_cache = [True] * limit # Sieve of Eratosthenes
    is_prime_cache[0] = is_prime_cache[1] = False # 0 and 1 are not primes

    for num in range(2, math.isqrt(limit) + 1):
        if is_prime_cache[num]:
            for multiplied in range(num ** 2, limit, +num):
                is_prime_cache[multiplied] = False
    
    prime_set = {num for num, prime in enumerate(is_prime_cache) if prime}

    return prime_set


def prime_factorization(number, prime):
    '''Recursive function to get the prime factorization of a number'''

    if number == 1:
        return []
    
    if number % prime == 0:
        return [prime] + prime_factorization(number // prime, prime)

    return []


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
    '''Find all of the permutations of the set, recursive function'''

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



def permutate_integers(array):
    '''Find all of the permutations of the set of integers, recursive function'''

    if len(array) == 1:
        return [array]

    permutations = []

    for n in range(len(array)):

        perm_start = array[n]
        remaining = array[:n] + array[n+1:]

        for p in permutate_integers(remaining):

            permutations.append([perm_start] + p)

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


def generate_polygonal_set(start, limit, formula):
    '''generate set of triangular numbers between start and limit'''

    result_set = set()
    n = 1

    current_num = 0

    while current_num < limit:

        current_num = int(formula(n))
        if current_num > start and current_num < limit:
            result_set.add(current_num)
        
        n += 1
    
    return result_set
    

def binomial_coefficient(m, n):
    '''Calculate number of subsets of size n from the set of size m'''

    if n > m:
        return
    
    coefficient = int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))

    return coefficient


def is_palindromic(num):
    '''Check if the number is palindromic'''

    string = str(num)

    if len(string) == 0:
        return False

    if len(string) == 1:
        return True

    # handle odd and even cases
    if len(string) % 2 == 0:
        midpoint = len(string) // 2
        first_half = string[:midpoint]
        second_half = string[midpoint:]
    else:
        midpoint = math.ceil(len(string) / 2) - 1
        first_half = string[:midpoint]
        second_half = string[midpoint + 1:]

    reverse_second = ''.join(reversed(second_half))

    if first_half == reverse_second:
        return True

    return False


def get_prime_factors(n, primes):
    '''non-recursive approach: primes argument MUST be sorted'''

    prime_factors = set()
    new_n = n

    for prime in primes:

        if prime > math.isqrt(n):
            break
        
        if new_n % prime == 0:

            prime_factors.add(prime)

            while new_n % prime == 0:
                new_n //= prime
    
    if new_n > 1:
        prime_factors.add(int(new_n))
    
    return prime_factors


def is_relatively_prime(num1, num2, primes):
    '''check if 2 numbers are co-prime'''

    # print("testing")

    # calculate divisors for each n
    for n in primes:

        if num1 % n == 0 and num2 % n == 0:
            return False
        
        if n > num1:
            return True
    
    return True


def totient_sieve(limit):
    '''Calculate sum of totient function phi(n) up to a limit'''

    phi = list(range(limit+1))

    for i in range(2, limit+1):

        if phi[i] == i: # this would mean it is prime

            for j in range(i, limit + 1, i):

                phi[j] -= phi[j] // i # reducing by each prime factor


    count = sum(phi) - 1 # reduce by 1 to remove the 1/1

    return count