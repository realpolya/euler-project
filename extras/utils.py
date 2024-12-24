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