'''
Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''

def digit_powers(digits=4):

    qualifying = []
    sum = 0
    max_limit = (9 ** int(digits)) * int(digits)

    for i in range(1, max_limit + 1):

        i_str = str(i)
        current_sum = 0

        for c in i_str:

            powered = int(c) ** int(digits)
            current_sum += powered

        if current_sum == i and i != 1:

            qualifying.append(i)
            sum += i
        
    return sum

print("Answer to problem 30: ", digit_powers(5))