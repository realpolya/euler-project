'''
Counting Summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''

# working with positive integers
# in how many ways can 100 be comprised of at least 2 positive integers

# combinatorics
# number theory


# establish a possible range

LIMIT = 5 # max number of integers for summation
MAX_INTEGERS = LIMIT
MIN_INTEGERS = 2


def list_integers(limit=LIMIT):

    integers = []

    for x in range(1, limit):
        integers.append(x)
    
    return integers


# take the greatest member of array
# try adding everything smaller to it
# if above the limit, move onto the next
# if below the limit, keep adding
# if at limit, add combination to the list of lists
# return len of lists

def count_summations(limit=LIMIT):

    integers = list_integers()

    print(integers)

count_summations()
