'''
Totient Maximum

Euler's totient function, phi(n) [sometimes called the phi function], 
is defined as the number of positive integers not exceeding n which 
are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than or equal to nine and relatively prime to nine, 
phi(9)=6.

It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.
Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

'''

# find a number of positive integers below n
# that are relatively prime to n

def is_relatively_prime(num1, num2):

    # divisors1 = set()
    # divisors2 = set()

    max_num = 0

    if num1 > num2:
        max_num = num1
    elif num2 > num1 or num1 == num2:
        max_num = num2

    # must not have common divisors greater than 1

    # calculate divisors for each n
    for n in range(2, max_num):

        divisor_true = [False, False]

        if num1 % n == 0:
            # divisors1.add(n)
            divisor_true[0] = True
        
        if num2 % n == 0:
            # divisors2.add(n)
            divisor_true[1] = True
        
        if all(divisor_true):
            return False

    # is there overlap?
    return True


def totient_max(limit=10):

    max_toti = 0

    for n in range(2, limit+1):

        prime_count = 1 # number 1 is already included

        for candidate in range(2, n):



    return max_toti


