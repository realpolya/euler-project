'''
Quadratic Primes

Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. 
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000 

where |n| is the modulus/absolute value of n 
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

'''

from extras.utils import is_prime


def quad_primes(limit):

    # longest chain variable
    max_chain = 0
    win_a = False
    win_b = False

    # for loop for a
    for a in range(-int(limit), int(limit)):

        # for loop for b
        for b in range(-int(limit), int(limit) + 1):

            n = 0
            broken = False
            current_chain = 0

            # consecutive values of n
            while not broken:

                candidate = n ** 2 + (a * n) + b # n^2 + an + b

                if not is_prime(candidate):
                    broken = True
                else:
                    current_chain += 1
                    n += 1

            if current_chain > max_chain:
                max_chain = current_chain
                win_a = a
                win_b = b
        
    # calculate product of the coefficients
    if win_a and win_b:

        return (win_a * win_b)
    
    return "not found"

print("Answer to problem 26: ", quad_primes(1000))