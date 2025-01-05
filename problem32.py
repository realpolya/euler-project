'''
Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

'''

def pandigital_sums(limit=10):

    sum = 0
    pan_products = []
    digits = []

    for n in range(1, limit):
        digits.append(n)

    for i in range(1, (limit * 10) + 1):

        for n in range(1, limit * 500):

            product = i * n

            if "0" in str(product):
                continue

            string = str(product) + str(i) + str(n)

            unique = []
            flag = False

            # check if all digits correspond and only once
            for char in string:

                if int(char) in unique:
                    flag = True
                    continue
                
                unique.append(int(char))

            if flag:
                continue

            if set(unique) != set(digits):
                continue

            # final case
            if product not in pan_products:
                sum += product
                pan_products.append(product)

    return sum   

print("Answer to problem 32: ", pandigital_sums())