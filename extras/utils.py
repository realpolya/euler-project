import math

# extra function
def is_prime(number):

    if number <= 1:
        return False 

    divisorFound = False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisorFound = True
            break

    if divisorFound:  
        # not a prime number
        return False

    return True


# version for without 0
def is_pandigital(n, required_set):

    unique = set()
    not_pan = False
    string = str(n)

    for char in string:
        num = int(char)
        if num in unique or num == 0:
            not_pan = True
            return not not_pan
        unique.add(num)
    
    if unique != required_set:
        not_pan = True
    
    return not not_pan