'''
Sub-string Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also 
has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. 
In this way, we note the following:

- d_2 d_3 d_4=406 is divisible by 2
- d_3 d_4 d_5=063 is divisible by 3
- d_4 d_5 d_6=635 is divisible by 5
- d_5 d_6 d_7=357 is divisible by 7
- d_6 d_7 d_8=572 is divisible by 11
- d_7 d_8 d_9=728 is divisible by 13
- d_8 d_9 d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''

from extras.utils import permutate, is_prime


def pass_checks(perm, primes):
    
    p = list(perm)

    approved = True
    i = 1

    for prime in primes:
        
        concat = int(p[i] + p[i + 1] + p[i + 2])

        if concat % prime != 0:
            approved = False
            return False
        
        i += 1
        
    if not approved:
        return False
    
    return approved


def substring_sum():

    final_sum = 0

    primes = []
    digits = []

    for n in range(2, 18):
        if is_prime(n):
            primes.append(n)
    
    for i in range(0, 10):
        digits.append(i)
    
    for perm in permutate(digits):

        if pass_checks(perm, primes):
            final_sum += int(perm)
    
    return final_sum
        

print("Answer to problem 43: ", substring_sum())