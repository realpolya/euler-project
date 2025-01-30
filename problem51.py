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


def binomial_coefficient(m, n):
    '''Calculate number of subsets of size n from the set of size m'''

    if n > m:
        return
    
    coefficient = int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))

    return coefficient
    

def digit_replacement(quantity=6):

    # find the first primes from the permutations
    # if multiple spaces are occupied, they are occupied with the same digit

    answer_sequence = []
    not_sequence = [] # storage for numbers that are already filtered out
    found = False
    family_size = 10 # there are always only 10 digits to iterate over
    cutoff = family_size - quantity # no point digging deeper beyond this point

    n = 10

    # cycle through primes

    # while not found:

    #     if is_prime(n):
            
    n = 56000223200 # example number

    # count digits
    digit_num = len(str(n))
    digit_indices = {}
    special_case = False # numbers with repeating digits
    special_vars_num = 0

    # variations are based on number of digits and repeating digits
    variations_num = digit_num # base (nmx, nxm, xnm)
    variations = []
    combo_indices_list = []
    
    if digit_num != len(set(str(n))) and digit_num > 2:

        special_case = True

        for i, char in enumerate(str(n)):

            if char in digit_indices:
                digit_indices[char].append(i)
            else:
                digit_indices[char] = [i]
        
        repeating_digits = {digit: indices for digit, indices in digit_indices.items() if len(indices) > 1}

        for digit, indices in repeating_digits.items():

            set_size = len(indices) # how many times does this digit repeat
            subset_size = set_size

            for _ in range(set_size - 1): # exclude cases where subset equals 1, they are already account for above

                special_vars_num += binomial_coefficient(set_size, subset_size)
                # print("set size is ", set_size, "subset_size is ", subset_size, "binomial coefficient is ", binomial_coefficient(set_size, subset_size))
                for subset in combinations(indices, subset_size):
                    combo_indices_list.append(subset)

                subset_size -= 1

    total_variations = variations_num + special_vars_num
    print("total variations ", total_variations, "special", special_vars_num)


    # for every variations generate a variation where the digit is replaced by i

    for i in range(variations_num):
        variation_list = list(str(n))
        variation_list[i] = "i"
        variation = "".join(variation_list)
        variations.append(variation)
    
    if special_case:
        for subset in combo_indices_list:
            variation_list = list(str(n))
            for i in subset:
                variation_list[i] = "i"
            variation = "".join(variation_list)
            variations.append(variation)
        
    print(len(variations))

    # special cases
    # if special_case:

            


        #     # FIXME: below
        #     # every constant number is labeled anything but x (i.e. n, m, j....)
        #     for front_back in range(2):

        #         prime_count = 0
        #         non_prime_count = 0
                
        #         sequence = []

        #         for i in range(10):

        #             # print("")
                    
        #             if front_back == 0: # first iteration
        #                 current = int(str(n) + str(i))
        #             else: # second iteration
        #                 if i == 0:
        #                     continue
        #                 current = int(str(i) + str(n))

        #             # count primes
        #             if is_prime(current):
        #                 prime_count += 1
        #                 sequence.append(current)
        #             else:
        #                 non_prime_count += 1

        #             # if number of primes is not meeting the quantity as compared to number of variations
        #             if non_prime_count > cutoff:
        #                 # abandon this route
        #                 break

        #             # if quantity is met - the first instance
        #             if prime_count == quantity:
                        
        #                 # assign to winning sequence
        #                 answer_sequence = sequence
        #                 found = True
                        
        
        # n += 1

    # return member 0 of winning sequence
    return answer_sequence

# print(digit_replacement())
digit_replacement()


# OLD SOLUTION
# while not found:
#     # while n < 10:

#         # establish a number of variations
#         # for 2 digits, 10 variations
#         variations = 10

#         # how many can be non-primes?
#         cutoff = variations - quantity

#         # n can be in front or behind
#         # start concatenating digits with digits from 0 to 9
#         for front_back in range(2):

#             prime_count = 0
#             non_prime_count = 0
            
#             sequence = []

#             for i in range(10):

#                 # print("")
                
#                 if front_back == 0: # first iteration
#                     current = int(str(n) + str(i))
#                 else: # second iteration
#                     if i == 0:
#                         continue
#                     current = int(str(i) + str(n))

#                 # count primes
#                 if is_prime(current):
#                     prime_count += 1
#                     sequence.append(current)
#                 else:
#                     non_prime_count += 1

#                 # if number of primes is not meeting the quantity as compared to number of variations
#                 if non_prime_count > cutoff:
#                     # abandon this route
#                     break

#                 # if quantity is met - the first instance
#                 if prime_count == quantity:
                    
#                     # assign to winning sequence
#                     answer_sequence = sequence
#                     found = True
                    
        
#         n += 1