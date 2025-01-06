'''
Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly 
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''

from extras.utils import is_prime


def check_fraction(num, den):
    '''Check if fraction is eligible for the digit cancelling fractions task'''

    if num > den or num == den:
        return False

    if num % 10 == 0 and den % 10 == 0:
        return False

    # see if it has the same digit, if not, continue
    overlap = any(char in str(den) for char in str(num))
    
    if not overlap:
        return False

    # what digit is overlapping
    canceled_digits = set(str(den)) & set(str(num))

    if len(canceled_digits) > 1:
        return False
    
    canceled_digit = next(iter(canceled_digits))

    count = 0
    for char in (str(den) + str(num)):
        if char == canceled_digit:
            count += 1
    
    if count > 2:
        return False
    
    # remove digit to see which fraction we have to get to
    new_num = int(str(num).replace(canceled_digit, ""))
    new_den = int(str(den).replace(canceled_digit, ""))

    if new_num == 0 or new_den == 0:
        return False
    
    return [num, den, new_num, new_den]



def prime_factorization(number, prime):
    '''Recursive function to get the prime factorization a number'''

    if number == 1:
        return []
    
    if number % prime == 0:
        return [prime] + prime_factorization(number // prime, prime)

    return []


def common_den(fractions):
    '''Find lowest common denominator among multiple fractions'''

    denos = [fraction[1] for fraction in fractions]
    primes = []

    for n in range(2, int((max(denos) / 2) + 1)):
        if is_prime(n):
            primes.append(n)
    
    # dictionary for powers
    prime_powers = {}
    
    for den in denos:
        for prime in primes:
            factors = prime_factorization(den, prime)

            if len(factors) > 0:
                count = factors.count(prime)
                if prime not in prime_powers or prime_powers[prime] < count:
                    prime_powers[prime] = count
    
    lcm = 1 # lowest common multiple
    for prime, power in prime_powers.items():
        lcm *= prime ** power
    
    return lcm
            


def cancel_fraction():
    '''Find the digit-cancelling fractions'''

    fractions = []

    for numerator in range(10, 100):

        for denominator in range(10, 100):

            eligible = check_fraction(numerator, denominator)
            if eligible:
                if (eligible[0] / eligible[1]) == (eligible[2] / eligible[3]):
                    fractions.append(eligible)
    
    pro_num = 1
    pro_den = 1
    for fraction in fractions:
        pro_num *= fraction[0]
        pro_den *= fraction[1]

    return int(pro_den / pro_num)


print("Answer to problem 33: ", cancel_fraction())