'''
Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

'''

def power_sum(power):

    product = 2 ** int(power)

    digits = list(str(product))

    # digits = [int(digit) for digit in digits]

    sum = 0
    for digit in digits:
        sum += int(digit)

    return sum

print("Answer to problem 16: ", power_sum(1000))