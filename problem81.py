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

from extras.utils import binomial_coefficient

def get_txt_matrix(file: str):

    rows = []

    with open(file, "r", encoding="utf-8") as f:
        rows = [[int(value) for value in line.strip().split(",")] for line in f if line.strip()]

    return rows


# TODO: try lattice paths, combinators, binomial coefficient

print("the length of rows is", len(get_txt_matrix("./extras/problem81_matrix.txt")))
print(get_txt_matrix("./extras/problem81_matrix.txt")[1])


print(binomial_coefficient(158, 79))