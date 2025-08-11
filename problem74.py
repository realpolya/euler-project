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


def get_the_sum(n):

    final_sum = 0

    # break the number into digits
    digits = list(str(n))

    # find factorial of each digit
    for digit in digits:

        # sum the factorials up
        final_sum += math.factorial(int(digit))

    return final_sum


def digit_chains(limit=200, target=5):

    # count non-repeating terms, initiate count
    count = 0

    # start loop up to the limit
    for n in range(1, limit + 1):

        # initiate local count
        local_count = 0

        # store non_repeating pattern in a set
        non_repeats = set()

        # a copy
        local_n = n
        
        # while loop? that would lead to nesting of a million within a million
        while local_n not in non_repeats:

            non_repeats.add(local_n)
            local_n = get_the_sum(local_n)
            local_count += 1

            if local_count > target:
                break

        # get the sum of the current_n
        if local_count == target:
            count += 1
    

    # return count
    return count


print(digit_chains(10**6, 60))