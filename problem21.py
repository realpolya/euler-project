'''
Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

import math

def divisors_sum(num):
    divisors = [1]
    sum = 0
    num = int(num)

    # cycle through numbers up to math.sqrt (inclusive)
    for i in range(2, int(math.sqrt(num) + 1)):

        # get the divisors
        if num % i == 0:
            # get the rest of the divisors by dividing by existing divisors
            new_divi = num / i
            divisors.extend([int(i), int(new_divi)])

    # add each divisors to the sum
    for divisor in divisors:

        sum += divisor
    
    # print("divisors are ", divisors)

    return sum


def amicable_pair(a, b):

    a = int(a)
    b = int(b)
    sum_a = divisors_sum(a)
    sum_b = divisors_sum(b)

        
    # if d(a) = b and d(b) = a
    if sum_a == b and sum_b == a:

        print("amicable pair", a, b)

        return a + b

    return False

def amicable_sums(limit):

    total_sum = 0

    # nested loops
    for i in range(limit):
        for j in range(i):

            if i == j:
                continue

            result = amicable_pair(i, j)
            if result:
                total_sum += result
    
    return total_sum

# amicable_pair(220, 284)
print(amicable_sums(10000))