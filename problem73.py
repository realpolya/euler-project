'''
Counting Fractions in a Range

Consider the fraction,  n/d, where n and d are positive integers. If n < d 
and {HCF}(n, d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
1/8,  1/7,  1/6,  1/5,  1/4,  2/7,  1/3, { 3/8,  2/5,  3/7},  1/2,  
4/7,  3/5,  5/8,  2/3,  5/7,  3/4,  4/5,  5/6,  6/7,  7/8

It can be seen that there are 3 fractions between  1/3 and  1/2.

How many fractions lie between  1/3 and  1/2 in the sorted set of reduced proper 
fractions for d <= 12,000?

'''

from fractions import Fraction
from extras.utils import sieve_eratosthenes, is_relatively_prime

def fractions_in_range(limit=8):

    # calculate primes
    primes = sieve_eratosthenes(limit)

    # establish range
    start_range = Fraction(1, 3)
    end_range = Fraction(1, 2)

    # start count of fractions in range
    count = 0

    # fracs = []
    fracs_set = set()

    # loop
    for d in range(2, limit+1):

        for n in range(int(d * start_range), int(d * end_range) + 1):

            if Fraction(n, d) <= start_range or Fraction(n, d) >= end_range:
                continue

            if Fraction(n, d) in fracs_set:
                continue

            if is_relatively_prime(n, d, primes):
                count += 1
                fracs_set.add(Fraction(n, d))
                # fracs.append(Fraction(n, d))
    
    # print(fracs)
    
    return count

# print(fractions_in_range())
print(fractions_in_range(12000))
# answer – 7390660
# 2nd answer – 7392464
# 3rd answer – 7295372
