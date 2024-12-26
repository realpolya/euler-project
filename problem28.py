'''
Number Spiral Diagonals

Starting with the number 1 and moving to the right in a 
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

'''
import math

def build_matrix(size):

    matrix = {} # 5x5, each row is represented as a key
    mid = int(size/2)

    for r in range(size):

        matrix[r] = [] # or set?

        for i in range(size):
            matrix[r].append("")
    
    matrix[mid][mid] = 1

    return matrix


def spiral(size=int(5)):

    matrix = build_matrix(size)
    mid = int(size/2)

    r = mid - 1 # start position for r
    i = mid + 1 # start position for i
    n = 1
    current = 2 # number of steps in each direction

    final_sum = 1

    for s in range(mid): # for every spiral

        for _ in range(current): # down
            n += 1
            r += 1
            matrix[r][i] = n

        final_sum += n

        for _ in range(current): # left
            n += 1
            i -= 1
            matrix[r][i] = n

        final_sum += n

        for _ in range(current):
            n += 1
            r -= 1
            matrix[r][i] = n
        
        final_sum += n

        for _ in range(current):
            n += 1
            i += 1
            matrix[r][i] = n
        
        final_sum += n

        # spiral ended
        current += 2
        i += 1 # move onto a new spiral
        r -= 1 # move onto a new spiral
    
    return final_sum

print("Answer to problem 28: ", spiral(1001))