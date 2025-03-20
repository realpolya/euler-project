'''
Cubic Permutations

The cube, 41063625 (345^3), can be permuted 
to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three 
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''

def produce_cube(limit=3):

    answer = False
    n = 233

    def check_eligibility(num, cube_1_list, digit_num):

        next_cube = 0
        while len(str(next_cube)) <= digit_num:

            


    # while loop
    while not answer:

        # cycle through numbers
        cube_1 = n ** 3
        # print(cube_1)

        cube_1_list = sorted(list(str(cube_1)))
        digit_num = len(cube_1_list) # digit limit
        # print(cube_1_list)

        # permutation has the same number of digits
        # sorted(list1) == sorted(list3)  # True

        # recursive function?
        cube_2 = 0
        while len(str(cube_2)) <= digit_num:


        # establish a limit for the cube to reach the max number of digits

        # if the limit is reached, move onto the next candidate

        # if permutation is found, then go into the cycle again to find the last permutation, starting with
        # the second candidate until the limit is reached, then abandon the candidate if no permutation is found

        n += 1
        answer = 1

    return answer

produce_cube()