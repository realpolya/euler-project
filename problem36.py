'''
Double-base Palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

import math


def is_palindromic(num):

    string = str(num)

    if len(string) == 1:
        return True

    midpoint = False
    first_half = False
    second_half = False

    if len(string) % 2 == 0:
        midpoint = len(string) // 2
        first_half = string[:midpoint]
        second_half = string[midpoint:]
    else:
        midpoint = math.ceil(len(string) / 2) - 1
        first_half = string[:midpoint]
        second_half = string[midpoint + 1:]

    # print ("first half is ", first_half, "second half is ", second_half)
    reverse_second = ''.join(reversed(second_half))
    if first_half == reverse_second:
        return True

    return False


def base_palindromes(limit=1000000):

    sum = 0

    for n in range(1, limit):

        if is_palindromic(n):

            # convert to binary
            binary_n = bin(n)[2:]

            if is_palindromic(binary_n):

                print("n", n, "is palindromic. binary n is ", binary_n)

                sum += n
    
    return sum

print(base_palindromes())