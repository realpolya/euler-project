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
long_matrix = get_txt_matrix("./extras/problem81_matrix.txt")


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


def get_pyramid(matrix: list, size: int):
    '''get the matrix into a dictionary with key-value pairs'''

    pyra_dict = {}

    # loop through the matrix
    for i_row, row in enumerate(matrix):
        for i_num, num in enumerate(row):
            current_key = i_row + i_num

            if current_key not in pyra_dict:
                pyra_dict[current_key] = []

            pyra_dict[current_key].append(num)

    for numbers in pyra_dict.values():
        numbers.reverse()

    print(pyra_dict)

    return pyra_dict


def count_min_sum(text_matrix, size):

    matrix = create_matrix(text_matrix, size)
    pyramid = get_pyramid(matrix, size)



count_min_sum(SAMPLE_MATRIX, 5)



# ------------------ OLD SOLUTION ------------------------

def reverse_path(matrix: list, size: int):
    '''try starting from the bottom of the matrix and reverse engineering the minimal sum path'''


    # current gets assigned to the bottom right number in the 2d matrix
    x = -1
    y = -1
    current = matrix[x][y]
    # variable for sum
    sum = current + matrix [0][0]
    moves = 0

    while moves < (size * 2) - 3:

        moves += 1

        if (y-1) < -size:
            # ignore up candidates, just sum up the left candidates
            left_candidate = matrix[x-1][y]
            sum += left_candidate
            current = left_candidate
            x -= 1
            continue

        if (x-1) < -size:
            up_candidate = matrix[x][y-1]
            sum += up_candidate
            current = up_candidate
            y -= 1
            continue
        
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

        print("current is", current)

    print("sum is", sum)

    return sum

    # always add the smaller one

    # move the current x



# reverse_path(matrix, 5)
# print(binomial_coefficient(158, 79))

# reverse_path(long_matrix, 80)