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


from sympy import symbols, expand


LIMIT = 6 # max number of integers for summation
MAX_INTEGERS = LIMIT


def list_integers(limit=LIMIT):

    integers = []

    for x in range(1, limit):
        integers.append(x)
    
    return integers



def partition_fn(integers=list_integers(), limit=LIMIT):

    # find coefficient of x to k
    x = symbols('x')

    print(x)

    expr = (1/(1-x)) * (1/(1-x**2)) * (1/(1-x**3))

    # print(expand(expr).coeff(x, 4))

    series_expansion = expr.series(x, 0, 5).removeO()

    print(series_expansion)

    print('coeff is ', series_expansion.coeff(x, 4))

    


partition_fn()


# count_summations()
# print(summation())


# -------------------- redundant --------------------------

def summation(integers=list_integers(), limit=LIMIT):

    print(integers)

    # keep track of the results
    results = []

    # TODO: need to increment the count
    results_count = 0

    # maximum index
    max_i = len(integers)

    def recursive_count(start, current_combo, current_sum):

        # handle base case
        if current_sum == limit:

            # results.append(list(current_combo))
            results.append(True)
            print("count is ", len(results))
            # print("results count is ", results_count)
            # results_count += 1
            return
        
        # limit exceeded - another base case
        if current_sum > limit:
            return
        
        # recursive loop
        for i in range(start, max_i):

            # include current integer in current combo
            current_combo.append(integers[i])

            # recurse with the updated sum
            # create a new branch
            # recursive count itself does not return anything
            # it just increases the corresponding count
            recursive_count(i, current_combo, current_sum + integers[i])

            # remove the last added number to explore the next branch 
            # with next integers[i] so it remains unaffected by this branch
            current_combo.pop()

    recursive_count(0, [], 0)

    # print(results)

    return len(results)

# take the greatest member of array
# try adding everything smaller to it
# if above the limit, move onto the next
# if below the limit, keep adding
# if at limit, add combination to the list of lists
# return len of lists

# def count_summations(limit=LIMIT):

#     integers = list_integers()

#     print(integers)

#     combinations = []
#     current_max = max(integers)

#     # print(current_max)

#     while current_max > 0:

#         current_max = max(integers)

#         for n in integers:

#             sum = current_max + n

#             while sum <= limit:
#                 sum += n 

#         integers.remove(current_max)