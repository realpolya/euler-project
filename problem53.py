'''
Combinatoric Selections

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 
5 
3 = 10.
In general, 

n 
r = {n!} / {r!(n-r)!}, where r <= n, 

n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million:  {23} {10} = 1144066.
How many, not necessarily distinct, values of  n r for 1 <= n <= 100, 
are greater than one-million?

'''

from extras.utils import binomial_coefficient


def combinatoric_selections(limit):

    counter = 0

    for n in range(1, limit + 1):

        for r in range(1, n + 1):

            coefficient = binomial_coefficient(n, r)

            if coefficient > 1000000:
                counter += 1
    
    return counter


print("Answer to problem 53: ", combinatoric_selections(100))
