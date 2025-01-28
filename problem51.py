'''
Prime Digit Replacements

By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, 
are all prime.

By replacing the 3rd and 4th digits of 56**3 
with the same digit, this 5-digit number is the first example having 
seven primes among the ten generated numbers, yielding the family: 56003, 
56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the 
first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an 
eight prime value family.

'''

from extras.utils import is_prime


def digit_replacement(quantity=6):

    # find the first primes from the permutations
    # if multiple spaces are occupied, they are occupied with the same digit
    answer_sequence = []
    found = False

    n = 1 # can be beginning or end
    # we can have m number of n's (as we do not know how 
    # many parts of the number are permanent)
    # iterable i can be anything

    # how many digits are in a number?
    # should we cycle through primes? TODO:

    # while loop
    while not found:
    # while n < 10:

        # establish a number of variations
        # for 2 digits, 10 variations
        variations = 10

        # how many can be non-primes?
        cutoff = variations - quantity

        # n can be in front or behind
        # start concatenating digits with digits from 0 to 9
        for front_back in range(2):

            prime_count = 0
            non_prime_count = 0
            
            sequence = []

            for i in range(10):

                # print("")
                
                if front_back == 0: # first iteration
                    current = int(str(n) + str(i))
                else: # second iteration
                    if i == 0:
                        continue
                    current = int(str(i) + str(n))

                # count primes
                if is_prime(current):
                    prime_count += 1
                    sequence.append(current)
                else:
                    non_prime_count += 1

                # if number of primes is not meeting the quantity as compared to number of variations
                if non_prime_count > cutoff:
                    # abandon this route
                    break

                # if quantity is met - the first instance
                if prime_count == quantity:
                    
                    # assign to winning sequence
                    answer_sequence = sequence
                    found = True
                    
        
        n += 1

    # return member 0 of winning sequence
    return answer_sequence

print(digit_replacement())