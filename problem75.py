'''
Singular Integer Right Triangles

It turns out that 12 cm is the smallest length of 
wire that can be bent to form an integer sided right 
angle triangle in exactly one way, but there are many more examples:

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, 
cannot be bent to form an integer sided right angle triangle, 
and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different 
integer sided right angle triangles:

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of 
L <= 1,500,000 can exactly one integer sided right angle triangle 
be formed:

'''

import math
from extras.utils import are_coprime

# a^2 + b^2 = c^2

# exactly one solution under 1.5 million
# what if there are more than 1 solutions? how do we check
# totient sieve?
# nested loops wouldn't work – too massive (1.5 million squared)


# add integers together a and b
# see if c is an integer?

# pythagorean theorem

# build my own sieve!


def primitive_triples(limit):
    '''New solution: generate primitive triples using Euclid's formula'''

    one_solution_cache = [False] * (limit+1)

    # m and n
    # m > n
    # m and n are co-prime
    # m - n is odd

    time_to_break = False

    # for m in range(1, int(limit/2)):
    for m in range(1, math.isqrt(limit) + 1):

        for n in range(1, m):

            if ((m - n) % 2) == 0:
                continue

            if not are_coprime(m, n):
                continue

            # a = m**2 - n**2
            # b = 2 * m * n
            # c = n**2 + m**2
            L = (m**2 - n**2) + (2 * m * n) + (n**2 + m**2)

            # print("now m is ", m, "n is ", n, "now L is ", L)

            if L > limit+1:
                time_to_break = True
                break


            # introduce multiple variable
            multiplier = 1
            multiple = L

            # take multiples of L length up until the end of the range
            while multiple <= limit:

                if one_solution_cache[multiple] == True:
                    # print("L of ", multiple, "has more than 1 solution!")
                    one_solution_cache[multiple] = False
                else:
                    # print("eliminating this now", multiple)
                    one_solution_cache[multiple] = True

                multiplier += 1
                multiple = L * multiplier
        
        if time_to_break:
            break
    
    # for i, item in enumerate(one_solution_cache):

    #     if item:
    #         print("for item", i, "the boolean is ", item)

    return sum(one_solution_cache)








# print(primitive_triples(100))
# print(primitive_triples(100000))
print(primitive_triples(1500000))


# --------------------------- OLD FUNCTION --------------------------------


def triangle_sieve(limit):

    # the version of solution below is correct but 
    # too slow for the desired limit

    # create a sieve
    one_solution_cache = [False] * (limit+1)

    multiples_b = set()
    multiples_a = set()

    # TODO: eliminate a and bs that are multiples of the original ones
    # can I reduce it ot O of n instead of n^3?

    # loop through a and b? a^2 + b^2 = c^2
    for b in range(2, int(1/3 * limit)):

        for a in range(math.isqrt(2*b + 1), b):

            print("dealing with a", a, "and b", b)

            if a in multiples_a and b in multiples_b:
                continue

            # sum of squares
            c_squared = a**2 + b**2

            # extract integer square root
            c = math.isqrt(c_squared)

            if c**2 == c_squared:

                # check passed, true square
                # calculate L wire length
                L = a + b + c

                # introduce multiple variable
                multiplier = 1
                multiple = L

                # print("L of ", L, "has at least one solution")

                # take multiples of L length up until the end of the range
                while multiple <= limit:

                    # if already true – permanently false
                    # if already True and finds it again, then it makes it False permanently
                    # more than 1 solution found!!
                    if one_solution_cache[multiple] == True:
                        # print("L of ", multiple, "has more than 1 solution!")
                        one_solution_cache[multiple] = False
                        # print("now the item is", one_solution_cache[multiple])
                    else:
                        one_solution_cache[multiple] = True

                    multiplier += 1
                    multiple = L * multiplier

                    # adding a and b
                    multiples_b.add(b * multiplier)
                    multiples_a.add(a * multiplier)
    
    # # print(one_solution_cache)
    # for i, item in enumerate(one_solution_cache):

    #     if item:
    #         print("for item", i, "the boolean is ", item)

    # return number of yes
    return sum(one_solution_cache)


# print(triangle_sieve(100))
# print(triangle_sieve(100000))