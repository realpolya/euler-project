'''
Path Sum: Two Ways

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by only moving to the right and down, 
is indicated in bold red and is equal to 2427.


131 673 234 103 18
201 96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37 331


Find the minimal path sum from the top left to the bottom 
right by only moving right and down in 
<a href="resources/documents/0081_matrix.txt">matrix.txt</a> 
(right click and "Save Link/Target As..."), a 31K text file containing an 
80 by 80 matrix.

'''

SAMPLE_MATRIX = '''131 673 234 103 18
201 96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37 331
'''

from extras.utils import binomial_coefficient

def get_txt_matrix(file: str):
    '''obtain the matrix from txt'''

    rows = []

    with open(file, "r", encoding="utf-8") as f:
        rows = [[int(value) for value in line.strip().split(",")] for line in f if line.strip()]

    return rows


# TODO: try lattice paths, combinators, binomial coefficient
# try reverse-engineering the path

# print("the length of rows is", len(get_txt_matrix("./extras/problem81_matrix.txt")))
# print(get_txt_matrix("./extras/problem81_matrix.txt")[1])


def create_matrix(text: str, size: int):
    '''turn a text-based matrix into a 2D list'''

    # create 2D array 
    matrix = [[] for _ in range(size)]

    lines = text.splitlines()

    if len(lines) > size:
        return

    for i, line in enumerate(lines):

        numbers = line.split()

        for number in numbers:

            matrix[i].append(int(number))

    print("matrix is", matrix)

    return matrix


def reverse_path(matrix: list, size: int):
    '''try starting from the bottom of the matrix and reverse engineering the minimal sum path'''



    # current gets assigned to the bottom right number in the 2d matrix
    x = -1
    y = -1
    current = matrix[x][y]
    # variable for sum
    sum = current
    moves = 0

    while moves < (size * 2) - 2:

        moves += 1

        up_candidate = matrix[x][y-1]
        left_candidate = matrix[x-1][y]

        # compare up_candidate and left_candidate
        if up_candidate < left_candidate:
            sum += up_candidate
            current = up_candidate
            y -= 1
        else:
            sum += left_candidate
            current = left_candidate
            x -= 1

    

    # always add the smaller one

    # move the current x



create_matrix(SAMPLE_MATRIX, 5)
# print(binomial_coefficient(158, 79))