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

import math
from itertools import combinations
from extras.utils import is_prime


def digit_replacement(quantity=6):

    answer_sequence = []
    found = False
    family_size = 10
    cutoff = family_size - quantity

    n = 11

    while not found:

        if is_prime(n) and len(set(str(n))) != 1:

            digit_num = len(str(n))
            digit_indices = {}
            special_case = False
            special_vars_num = 0

            # base variations (nmx, nxm, xnm)
            variations_num = digit_num
            variations = []
            combo_indices_list = []
            
            # if any digits repeat, calculate special variations
            if digit_num != len(set(str(n))) and digit_num > 2:

                special_case = True

                for i, char in enumerate(str(n)):

                    if char in digit_indices:
                        digit_indices[char].append(i)
                    else:
                        digit_indices[char] = [i]
                
                repeating_digits = {digit: indices for digit, indices in digit_indices.items() if len(indices) > 1}

                for digit, indices in repeating_digits.items():

                    set_size = len(indices)
                    subset_size = set_size

                    for _ in range(set_size - 1): # exclude cases where subset equals 1, they are already accounted for above

                        for subset in combinations(indices, subset_size):
                            combo_indices_list.append(subset)

                        subset_size -= 1

            total_variations = variations_num + special_vars_num

            # standard variations
            for i in range(variations_num):

                variation_list = list(str(n))
                variation_list[i] = "i"
                variation = "".join(variation_list)
                variations.append(variation)
            
            # repeating numbers variations
            if special_case:

                for subset in combo_indices_list:
                    variation_list = list(str(n))
                    for i in subset:
                        variation_list[i] = "i"
                    variation = "".join(variation_list)
                    variations.append(variation)

            # replacing "i" with digits, counting primes
            for variation in variations:

                primes_counter = 0
                not_primes = 0
                not_answer = False
                current_sequence = []

                for digit in range(10):

                    variation_list = list(variation)

                    if digit == 0 and variation_list[0] == "i":
                        continue

                    new_digits = [str(digit) if char == "i" else char for char in variation_list]
                    new_number = int("".join(new_digits))

                    if is_prime(new_number):
                        primes_counter += 1
                        current_sequence.append(new_number)
                    else:
                        not_primes += 1
                    
                    if not_primes > cutoff:
                        not_answer = True
                        break
                    
                if primes_counter >= quantity:
                    answer_sequence = current_sequence
                    found = True
                    break

        n += 1

    # return member 0 of winning sequence
    return answer_sequence[0]



print("Answer to problem 51: ", digit_replacement(8))