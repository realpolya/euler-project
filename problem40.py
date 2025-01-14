'''
Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910 1 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n-th digit of the fractional part, find the value of the following expression.

d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1 000 000

'''

def concat_fraction(limit=1000000):
    '''Find the product of the requested digits of the irrational fraction'''

    stops = [1, 10, 100, 1000, 10000, 100000, 1000000]
    candidates = []

    counter = 0
    n = 1

    # loop method
    while counter <= limit:

        string = str(n)

        # increment the counter
        for char in string:
            counter += 1
            if counter in stops:
                candidates.append(int(char))

        # increment n
        n += 1
    
    product = 1
    for digit in candidates:
        product *= digit
    
    return product

print("Answer to problem 40: ", concat_fraction())