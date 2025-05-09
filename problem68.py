'''
Magic 5-gon Ring

'''

from itertools import combinations
from extras.utils import permutate, binomial_coefficient


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


def gon_ring(ring_num=3):

    # calculate digits
    digits = [1]
    for n in range(2, (ring_num * 2) + 1):
        digits.append(n)
    
    start_permutations = []
    
    # find possible start triplets/triads
    # possible_sets = binomial_coefficient(6, 3)

    triads = combinations(digits, 3)
    for subset in triads:

        triad_permutations = permutate(list(subset))
        # print("for subset ", subset, "permutations are ", triad_permutations)

        for triad in triad_permutations:
            start_permutations.append(triad)
    
    print(len(start_permutations))

    solutions = set()

    # cycle through start permutations
    for first_triad in start_permutations:

        # create a list view of the triad
        first_triad_list = [int(n) for n in list(first_triad)]

        # calculate the sum of the triad
        first_sum = sum(first_triad_list)

        # establish available remaining digits
        remaining_digits = get_remaining_digits(digits, first_triad_list)
        
        # last digit is middle of second
        second_triad = [0, first_triad_list[2], 0]

        # try different digits for 0s in second triad, see if the sum is the same
        # FIXME: recursive function!!!
        second_candidates = combinations(remaining_digits, 2)
        second_permutations = []
        for subset in second_candidates:

            permutations = permutate(list(subset))

            for diad in permutations:
                second_permutations.append(diad)
        
        # cycle through permutations
        for second_candidate in second_permutations:

            second_triad = [int(second_candidate[0]), first_triad_list[2], int(second_candidate[1])]
            second_sum = sum(second_triad)

            if second_sum == first_sum:
                # print("sum ", second_sum, "first triad is ", first_triad_list, "second triad is ", second_triad)

                for digit in remaining_digits:
                    if digit not in second_triad:
                        last_digit = digit
                
                # middle digit of first is last of last – 0 placeholder
                # last digit of second is middle digit of second
                last_triad = [last_digit, second_triad[2], first_triad_list[1]]
                third_sum = sum(last_triad)

                if third_sum == second_sum:
                    # print("sum", third_sum, "solution: ", first_triad_list, second_triad, last_triad)

                    # establish lowest value
                    solution = [get_int_from_str(first_triad_list), get_int_from_str(second_triad), get_int_from_str(last_triad)]
                    # print(solution)

                    lowest_term = 10000
                    for term in solution:
                        if term < lowest_term:
                            lowest_term = term
                    
                    if lowest_term == solution[0]:
                        print("solution is ", solution, "sum is ", third_sum)
                        solutions.add(get_int_from_str(solution))
        

    print(solutions)

    return max(solutions)


        # how many triads ? depends on the ring_num






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
    


print(gon_ring())