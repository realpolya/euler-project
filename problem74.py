'''
Digit Factorial Chains

The number 145 is well known for the property that the sum of the 
factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145.

Perhaps less well known is 169, in that it produces the longest 
chain of numbers that link back to 169; it turns out that there 
are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will 
eventually get stuck in a loop. For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number 
below one million is sixty terms.

How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?

'''

import math

# TODO: what is the factorial of 0? 0! = 1?

def get_the_sum(n):

    final_sum = 0

    # break the number into digits
    digits = list(str(n))

    # find factorial of each digit
    for digit in digits:

        # sum the factorials up
        final_sum += math.factorial(int(digit))

    # repeat
    return final_sum

print(get_the_sum(145))
print(get_the_sum(169))