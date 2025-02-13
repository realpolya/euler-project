'''
Powerful Digit Sum

A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is 
the maximum digital sum?

'''

def powerful_digit_sum(limit=100):

    max_sum = 0

    for a in range(limit):
        for b in range(limit):

            power_num = a ** b
            digi_sum = 0

            for char in str(power_num):

                digi_sum += int(char)
            
            if digi_sum > max_sum:

                max_sum = digi_sum
    
    return max_sum

print("Answer to problem 56: ", powerful_digit_sum())