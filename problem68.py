'''
Magic 5-gon Ring

'''

from itertools import combinations
from extras.utils import permutate_integers


def get_int_from_str(list):

    string = ""

    for x in list:
        string += str(x)
    
    return int(string)



def get_remaining_digits(digits, triad):

    available_digits = set()

    for digit in digits:
        if digit not in triad:
            available_digits.add(digit)

    return available_digits



def branch(remaining_digits, first_sum, limit, middle_num, first_triad, counter=0, current_candidates=None, all_solutions=None):
    '''find middle candidates' validity via recursive function'''
    
    if current_candidates is None:
        current_candidates = []
    if all_solutions is None:
        all_solutions = []

    # handle base cases
    if counter == limit:
        return [current_candidates[:]]

    new_candidates = combinations(remaining_digits, 2)
    new_permutations = []

    for subset in new_candidates:

        permutations = permutate_integers(list(subset))

        for diad in permutations:
            new_permutations.append(diad)
        
    # cycle through permutations (2 candidates)
    for new_candidate in new_permutations:

        # create a list view of the triad
        new_triad = [int(new_candidate[0]), middle_num, int(new_candidate[1])]

        # calculate the sum of the triad
        new_sum = sum(new_triad)
        
        # check the validity of sums
        if new_sum == first_sum:

            new_current = current_candidates[:] + new_triad
            new_remaining_digits = get_remaining_digits(remaining_digits, new_triad)
            new_middle_num = int(new_candidate[1])

            solution = branch(new_remaining_digits, first_sum, limit, new_middle_num, first_triad, counter + 1, new_current)
            
            if solution:
                all_solutions.extend(solution)


    if all_solutions:
        return all_solutions 
        
    return False


            

def gon_ring(ring_num=5):

    # number of repetitions in the middle
    middle_repetitions = ring_num - 2

    digits = [1]
    for n in range(2, (ring_num * 2) + 1):
        digits.append(n)
        
    start_permutations = []
    triads = list(combinations(digits, 3))

    for subset in triads:

        triad_permutations = permutate_integers(list(subset))

        for triad in triad_permutations:
            start_permutations.append(triad)
    
    solutions = set()

    # cycle through START permutations
    for first_triad in start_permutations:

        # calculate the sum of the triad
        first_sum = sum(first_triad)

        # establish available remaining digits
        remaining_digits = get_remaining_digits(digits, first_triad)

        viable_branches = branch(remaining_digits, first_sum, middle_repetitions, first_triad[2], first_triad)

        if viable_branches:

            for viable_branch in viable_branches:

                penultimate_triad = viable_branch[-3:]

                last_digit = next(iter(get_remaining_digits(remaining_digits, viable_branch)))

                last_triad = [last_digit, penultimate_triad[2], first_triad[1]]
                last_sum = sum(last_triad)

                if ring_num == 5:
                    triad_3 = viable_branch[-6:-3]
                    triad_2 = viable_branch[-9:-6]

                if last_sum == first_sum:
                    
                    # solution for a 5 ring, adjust the following variable
                    # to get a solution for other numbers
                    solution = [get_int_from_str(first_triad), 
                        get_int_from_str(triad_2),
                        get_int_from_str(triad_3),
                        get_int_from_str(penultimate_triad),
                        get_int_from_str(last_triad)
                    ]

                    lowest_term = 10000
                    for term in solution:
                        if term < lowest_term:
                            lowest_term = term
                    
                    if lowest_term == solution[0]:
                        solutions.add(get_int_from_str(solution))

    # a solution should be a 16-digit string
    sixteen = set()
    for solution in solutions:

        long_string = str(solution)

        if len(long_string) == 16:
            sixteen.add(solution)

    return max(sixteen)



print("Answer to problem 68: ", gon_ring())



    
# -----------------------------------------------------------------




# def gon_ring(ring_num=3):

#     # number of repetitions in the middle
#     middle_repetitions = ring_num - 2

#     # calculate digits
#     digits = [1]
#     for n in range(2, (ring_num * 2) + 1):
#         digits.append(n)
    
#     start_permutations = []
    
#     # find possible start triplets/triads
#     # possible_sets = binomial_coefficient(6, 3)

#     triads = combinations(digits, 3)
#     for subset in triads:

#         triad_permutations = permutate(list(subset))
#         # print("for subset ", subset, "permutations are ", triad_permutations)

#         for triad in triad_permutations:
#             start_permutations.append(triad)
    
#     print(len(start_permutations))

#     solutions = set()

#     # cycle through START permutations
#     for first_triad in start_permutations:

#         # create a list view of the triad
#         first_triad_list = [int(n) for n in list(first_triad)]

#         # calculate the sum of the triad
#         first_sum = sum(first_triad_list)

#         # establish available remaining digits
#         remaining_digits = get_remaining_digits(digits, first_triad_list)
        
#         # last digit is middle of second
#         second_triad = [0, first_triad_list[2], 0]

#         # try different digits for 0s in second triad, see if the sum is the same
#         # FIXME: recursive function!!! ---------------------------------

#         second_candidates = combinations(remaining_digits, 2)
#         second_permutations = []

#         for subset in second_candidates:

#             permutations = permutate(list(subset))

#             for diad in permutations:
#                 second_permutations.append(diad)
        
#         print(second_permutations)
        
#         # cycle through permutations (2 candidates)
#         for second_candidate in second_permutations:

#             # create a list view of the triad
#             second_triad = [int(second_candidate[0]), first_triad_list[2], int(second_candidate[1])]

#             # calculate the sum of the triad
#             second_sum = sum(second_triad)
            
#             # check the validity of sums
#             if second_sum == first_sum:
#                 # print("sum ", second_sum, "first triad is ", first_triad_list, "second triad is ", second_triad)

#                 # establish the last digit for the last step
#                 for digit in remaining_digits:
#                     if digit not in second_triad:
#                         last_digit = digit
                
#                 # middle digit of first is last of last – 0 placeholder
#                 # last digit of second is middle digit of second
#                 last_triad = [last_digit, second_triad[2], first_triad_list[1]]
#                 third_sum = sum(last_triad)

#                 if third_sum == second_sum:
#                     # print("sum", third_sum, "solution: ", first_triad_list, second_triad, last_triad)

#                     # establish lowest value
#                     solution = [get_int_from_str(first_triad_list), get_int_from_str(second_triad), get_int_from_str(last_triad)]
#                     # print(solution)

#                     lowest_term = 10000
#                     for term in solution:
#                         if term < lowest_term:
#                             lowest_term = term
                    
#                     if lowest_term == solution[0]:
#                         print("solution is ", solution, "sum is ", third_sum)
#                         solutions.add(get_int_from_str(solution))
        

#     print(solutions)

#     return max(solutions)


#         # how many triads ? depends on the ring_num






    # structure of the ring

    # ring_num of triplets, last digit of triplet is the middle of the next
    # only those repeat throug the structure

    # permutations
    # first permutation decides the middle num for the second one, 
    # decides the last number for the last one
    # remaining digits?

    # check if second permutation has the same sum
    # check if third permutation has the same sum
    # for gon_ring number of rings, check for the same sum

    # if checks clear, then 


# def next_candidates(limit, permutations, digits, first=False):

#     if limit == 0:
#         return 
    
#     if 
    


# print(gon_ring())