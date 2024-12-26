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

def spiral(size=int(5)):

    matrix = {} # 5x5, each row is represented as a key
    mid = int(size/2)

    for r in range(size):

        matrix[r] = [] # or set?

        for i in range(size):
            matrix[r].append("")
    
    matrix[mid][mid] = 1
    print(matrix)
    

    # for spiral in range(int(size / 2) + 1):

    #     print(math.ceil(size/2))

    


spiral()


