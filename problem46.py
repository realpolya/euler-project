'''
Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every 
odd composite number can be written as the sum of a prime 
and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot 
be written as the sum of a prime and twice a square?

'''

import math
from extras.utils import is_prime

def find_fault():

    # sum of a prime and twice a square
    answer = False
    n = 3
    primes = [2]

    while not answer:

        if not is_prime(n):

            composite_clear = False

            for prime in primes:

                remainder = int((n - prime) / 2)

                if math.sqrt(remainder).is_integer() or remainder == 1:
                    composite_clear = True
                    break
            
            if not composite_clear:
                answer = n
        
        else:
            primes.append(n)

        n += 2
    
    return answer


print("Answer to problem 46: ", find_fault())