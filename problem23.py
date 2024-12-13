'''
Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Wikipedia: 20161 is the limit

'''

from extras.abu_sums import ABU_SUMS

def is_abundant(num):
    '''Check if number is abundant'''

    divisors = []
    sum = 0

    # find all of the divisors
    for i in range(1, num):

        if num % i == 0:
            divisors.append(i)
            sum += i
    
    return sum > num


def abundant_nums(limit=20161):
    '''Find all of the abundant numbers below the limit'''

    abundant = [] # list of abundant numbers
    abu_sums = set()

    for i in range(12, limit - 11):
        if is_abundant(i):
            abundant.append(i)

    for n in abundant:

        if n > limit / 2:
            break
        
        above_limit = False

        for m in abundant:

            if m < n:
                continue

            sum = n + m
            if (sum) >= limit:
                above_limit = True
                break
            
            if sum not in abu_sums:
                abu_sums.add(sum)

        if above_limit:
            continue
    

    return abu_sums


def non_abu_sum(limit=20162, abu_sums=ABU_SUMS):
    '''Find the sum of all non-abundant integers'''

    non_abu_sums = set()
    sum = 0

    for i in range(1, limit):
        if i not in abu_sums:
            non_abu_sums.add(i)
            sum += i

    return sum

print("Answer to problem 23: ", non_abu_sum())