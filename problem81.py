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


def get_min_sum(dict, size):
    '''get minimal path sum – adapted from problem 18 maximum path sum'''

    # create a copy of dictionary
    new_dict =  dict.copy()
    current_count = 0 # counting when the center of the pyramid is reached

    for i in range(len(new_dict.keys()) - 2, -1, -1): # start at row second to last, end at 0
        
        # interior loop for every row
        for index, num in enumerate(new_dict[i]):

            if current_count < size - 1:

                # TODO:

                if index == 0:

                    # First element: only one neighbor
                    new_dict[i][index] += new_dict[i+1][index]

                elif index == len(new_dict[i]) - 1:
                    # Last element: only one neighbor
                    new_dict[i][index] += new_dict[i+1][index-1]

                else:
                    # Middle elements: choose the smaller of two neighbors
                    new_dict[i][index] += min(
                        new_dict[i+1][index-1],
                        new_dict[i+1][index]
                    )

            else:

                # compare the options below
                if new_dict[i+1][index] < new_dict[i+1][index+1]:

                    new_dict[i][index] += new_dict[i+1][index]
                
                elif new_dict[i+1][index] >= new_dict[i+1][index+1]:

                    new_dict[i][index] += new_dict[i+1][index+1]

        current_count += 1
                
    return new_dict[0][0]



def count_min_sum(matrix, size):

    # matrix = create_matrix(text_matrix, size)
    pyramid = get_pyramid(matrix, size)

    # print("pyramid is", pyramid)
    pyramid_min_sum = get_min_sum(pyramid, size)
    print(pyramid_min_sum)

    # count the min sum of the top half of the pyramid

    # separate by the number of keys
    # top_pyramid = {key: value for key, value in pyramid.items() if key < size}
    # bottom_pyramid = {key: value for key, value in pyramid.items() if key >= size}

    # # print("this is top_pyramid", top_pyramid)
    # print("this is bottom_pyramid", bottom_pyramid)

    # top_pyramid_min_sum = get_min_sum(top_pyramid)
    # print("top pyramid min sum is ", top_pyramid_min_sum)

    # # copy bottom pyramid
    # bottom_copy = {key: values.copy() for key, values in bottom_pyramid.items()}

    # shifted_bottom = {key - size: value for key, value in bottom_copy.items()}
    # last_key = max(shifted_bottom)
    # reversed_bottom = {
    #     last_key - key: value for key, value in shifted_bottom.items()
    # }

    # reversed_bottom_pyramid = dict(sorted(reversed_bottom.items()))

    # # print(reversed_bottom_pyramid)


    # bottom_pyramid_min_sum = get_min_sum(reversed_bottom_pyramid)

    # print("bottom pyramid min sum is ", bottom_pyramid_min_sum)

    # print("min sum total", top_pyramid_min_sum + bottom_pyramid_min_sum)





count_min_sum(long_matrix, 80)



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