'''
Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

'''

import math

def find_c(a, b, p):
    '''Test if there is a 'c' for the combination of a, b, and perimeter'''

    c = p - a - b
    if c**2 == a**2 + b**2:
        return c
    
    return False


def max_solutions(limit=150):
    '''Find perimeter with the max number of a, b, and c solutions'''

    max_solutions = 0
    winner_p = 0

    for p in range(1, limit + 1):

        solutions_num = 0

        for b in range(1, p):
            for a in range(1, b):

                c = find_c(a, b, p)
                if c:
                    solutions_num += 1
                
        if solutions_num > max_solutions:
            max_solutions = solutions_num
            winner_p = p
    
    return winner_p


print("Answer to problem 39: ", max_solutions(1000))