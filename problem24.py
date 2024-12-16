'''
Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

import math
# from itertools import permutations

def permutate(array):

    if len(array) == 1:
        print("Base case reached: ", array)
        return str(array[0])

    permutations = []
    answer = False

    # number of permutations equals to factorial of length
    perm_num = math.factorial(len(array))

    for n in range(len(array)):

        perm_start = array[n]

        too_long = False

        print("perm start is ", perm_start)

        remaining = array[:n] + array[n+1:]
        print("remaining is ", remaining)

        for p in permutate(remaining):

            print("doing recursion on ", p)
            string = "".join(str(perm_start) + str(p))
            permutations.append(string)

    
            if len(permutations) >= 1000000:

                too_long = True
                break

        if too_long:

            break

    return permutations





def lexi_perm(limit):

    digits = []
    permutations = []

    for i in range(limit+1):
        digits.append(i)
    
    # print(digits)

    perms = permutate(digits)

    # print(perms)

    return perms[999999]





print("answer is", lexi_perm(9))