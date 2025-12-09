'''
Passcode Derivation

A common security method used for online 
banking is to ask the user for three random characters 
from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; 
the expected reply would be: 317.

The text file contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest 
possible secret passcode of unknown length.

'''

# topological sort idea: Directed Acyclic Graph (DAG)

from extras.problem79_extra import ATTEMPTS


def is_subsequence(main, incoming):
    '''check that incoming list is in the same order as main'''

    it = iter(main)

    return all(x in it for x in incoming)


def reorder_list(new_att, passcode):

    # if subsequence has the same order as passcode
    if is_subsequence(passcode, new_att):
        return passcode

    # identifying new digits
    extras = [x for x in new_att if x not in passcode]
    reordered = [x for x in new_att if x in passcode]

    # if no overlap between new_att and passcode
    if len(reordered) == 0:
        reordered = passcode + extras
        return reordered

    # if digits exist and need reordering
    pass_copy = list(passcode) + extras

    for a, b in zip(new_att, new_att[1:]):

        # get indices for a and b in the passcode
        ia = pass_copy.index(a)
        ib = pass_copy.index(b)

        # if in passcode index of a precedes index of b, change order
        if ia > ib:
            pass_copy.pop(ia)
            ib = pass_copy.index(b)
            pass_copy.insert(ib, a)
        
    return pass_copy


def analyze_attempts(attempts=ATTEMPTS):

    passcode = []
    rulebook = [] # attempts already covered
    first = True

    for attempt in attempts:

        att_list = list(str(attempt))

        if first:
            passcode.extend(att_list)
            first = False

        # keep reordering list with every attempt
        passcode = reorder_list(att_list, passcode)

        # add to rulebook the baked rule
        rulebook.append(att_list)


    # double check that the rulebook was followed
    for attempt in attempts:

        if not is_subsequence(passcode, list(str(attempt))):
            print("ERROR")

    return ''.join(passcode)


print("Answer to problem 79: ", analyze_attempts())







# -----------------------------extras--------------------


# compare every two attempts, then merge and compare every four (up until you have all 50)

# def compare_lists(list1, list2):
#     ''' compare two lists of numbers and return a combination with possible order '''

#     new_order = list1.copy()

#     for digit in list2:

#         if digit not in new_order:
#             new_order.append(digit)
        
#     # 680 and 180 can return two possibilities: 6180 and 1680


# branching would become too extreme (tree too large)


# def derive_brute_force():

#     # get all of the possible digits
#     possible_digits = set()

#     for attempt in ATTEMPTS:
#         digits = list(str(attempt))

#         for digit in digits:
#             possible_digits.add(digit)
    
#     print(possible_digits)

#     print(len(ATTEMPTS))
#     print(math.factorial(8))
#     print(math.factorial(8) * len(ATTEMPTS))

#     factorial_obj = {}

#     factorial_digits = list(possible_digits)

#     possible_combos = combinations(factorial_digits, 8) # FIXME: get all possible combos with all digits
#     # print(possible_combos)

#     for combo in possible_combos:
#         print("hello", combo)



# derive_brute_force()





# def derive_passcode():
#     # the numbers are always in order

#     # initiate a passcode variable
#     passcode = ''
#     passcode_arr = []

#     count = 0 # temp count

#     # loop through attempts
#     for attempt in ATTEMPTS:

#         digits = list(str(attempt))
        
#         # loop through digits
#         for i, digit in enumerate(digits):

#             # if digit is not seen before, concatenate
#             if str(digit) not in passcode:

#                 passcode += str(digit)
#                 passcode_arr.append(digit)

#             # if digit is seen before
#             elif str(digit) in passcode:

#                 # compare indices in passcode array and in digits list


#                 # loop through passcode digits

#                 # compare order of the digits

#                 # must not contradict previous attempts
        
#         count += 1

#         if count > 2:
#             break

#     # follow the order of digits until something does not click

#     print(passcode)
#     print(passcode_arr)




# # print(ATTEMPTS)

# derive_passcode()