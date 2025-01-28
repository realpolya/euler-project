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

def digit_replacement(quantity):

    # find the first primes from the permutations
    # if multiple spaces are occupied, they are occupied with the same digit
    answer_sequence = []

    # while loop
    
        # loop through numbers

        # if is_prime

            # establish a number of variations

            # start replacing digits with digits from 0 to 9

                # count primes

                # if number of primes is not meeting the quantity as compared to number of variations

                    # abandon this route

                # if quantity is met

                    # assign to winning sequence

    # return member 0 of winning sequence
    return answer_sequence

                