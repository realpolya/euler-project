'''
Coin Partitions

Let p(n) represent the number of different ways in 
which n coins can be separated into piles. 
For example, five coins can be separated into
piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which 
p(n) is divisible by one million.

'''

from extras.utils import generate_polygonal_set
from extras.polygonal import pentagonal_formula

COINS = 5
DIVISIBLE_LIMIT = 10**6


# goal: p(n) % DIVISIBLE_LIMIT == 0
# what is n?
# p(coins) = number of ways

def coin_partitions(modulo=DIVISIBLE_LIMIT):

    # use pentagonal number theorem
    negative = True
    pentagonals = generate_polygonal_set(1, 20, pentagonal_formula, negative)
    print(sorted(pentagonals))


coin_partitions()
# print("Answer is: ", coin_partitions())



#-------------------------irrelevant---------------------------

# def coin_partitions():


#     # new_dp_list = dynamic_programming(limit)

#     # print("new dp list is ", new_dp_list)

#     # new_list = new_dp_list.copy()

#     # dp = [1]

#     # # for i in range(1, 6):
#     # #     dp = dynamic_programming_existing(dp, i)
#     # #     print(f"After coin {i}:", dp)

#     # print("the correct dp list for 5 is ", dynamic_programming(5))

#     # # initiate dp_list
#     # # dp_list = dynamic_programming(limit)
    
#     # # print(dp_list)

#     limit = 1
#     # final condition
#     divisible = False

#     answer = 0
#     subdivision = 100000
#     modulo = DIVISIBLE_LIMIT

#     while not divisible:

#         print("amount of coins is now ", limit)

#         dp_list = dynamic_programming(limit, modulo)

#         last_ten_thousand = dp_list[-subdivision:]
#         for result in last_ten_thousand:

#             if result == 0:
#                 print("found, result is ", result)
#                 part_answer = result
#                 # answer = limit
#                 divisible = True
        
#         if divisible:
#             for i, value in dp_list:
#                 if value == part_answer:
#                     answer = i
        
#         print("the last result for the last coin now is ", dp_list[-1])
#         limit += subdivision
        
#     return answer






#     # # we don't know how many n coins, aka what is the limit?
#     # # it needs to be a while loop

#     # # initiate dp list
#     # dp_list = [1]

#     # # final condition
#     # divisible = False

#     # # initiate coins (n) and amount

#     # # start the while loop
#     # while not divisible:

#     #     # append new element to dp_list
#     #     dp_list.append(0)

#     #     # interior loop for amount
#     #     for amount in range()

#     #     # check for divisibility of the added element
#     #     if 

#     #     # increment coins