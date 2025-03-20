'''
Cubic Permutations

The cube, 41063625 (345^3), can be permuted 
to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three 
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''


def eligible_num(n, cube_1_list, digit_num):
    '''check whether n is eligible to to be the right answer'''

    next_cube = 0
    eligible = False
    num = n + 1
    
    while len(str(next_cube)) <= digit_num and not eligible:

        next_cube = num ** 3
        next_cube_list = sorted(list(str(next_cube)))
        # print("num is ", num, "n is ", n, "cube 1 list is ", cube_1_list, "next cube list is", next_cube_list)

        if next_cube_list == cube_1_list:
            # print("num is ", num, "n is ", n, "cube 1 list is ", cube_1_list, "next cube list is", next_cube_list)
            # print("found a permutation")
            eligible = True
        else:
            num += 1
    
    if not eligible:
        num = 0

    return num



def produce_cube(limit=3):


    answer = False
    smallest_cube = 0
    n = 1


    # while loop
    while not answer:

        # cycle through numbers
        cube_1 = n ** 3
        # print(cube_1)

        cube_1_list = sorted(list(str(cube_1)))

        # establish a limit for the cube to reach the max number of digits
        digit_num = len(cube_1_list) # digit limit
        # print(cube_1_list)

        eligible = True
        current_n = n
        for _ in range(limit - 1):
            current_n = eligible_num(current_n, cube_1_list, digit_num)
            if not current_n:
                eligible = False
                break

        # if permutation is found, then go into the cycle again to find the last permutation, starting with
        # the second candidate until the limit is reached, then abandon the candidate if no permutation is found
        if eligible:
            # print("n is ", n)
            answer = True
            smallest_cube = cube_1
        
        # if n == 345:
        #     answer = True

        n += 1


    return smallest_cube

print(produce_cube())