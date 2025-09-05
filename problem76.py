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

def list_integers(limit=5):

    integers = []

    for x in range(1, limit):
        integers.append(x)
    
    return integers

