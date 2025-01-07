'''
Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

'''

import math

def digit_factorials():

    # establish a limit with factorials of 9
    # 9 999 999 = impossible to reach with summing the factorials
    # limit of 1 million (999 999)

    curious_nums = []
    global_sum = 0

    for n in range(3, 1000000):

        sum = 0

        for char in str(n):

            sum += math.factorial(int(char))
        
        if sum == n:
            curious_nums.append(n)
            global_sum += n
        
    print(curious_nums)
    return global_sum


print("Answer to problem 34: ", digit_factorials())