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

from extras.utils import dynamic_programming


COINS = 5
DIVISIBLE_LIMIT = 10**6


# goal: p(n) % DIVISIBLE_LIMIT == 0
# what is n?
# p(coins) = number of ways

def coin_partitions():

    limit = 1

    # initiate dp_list
    # dp_list = dynamic_programming(limit)
    
    # print(dp_list)

    # final condition
    divisible = False

    answer = 0

    while not divisible:

        dp_list = dynamic_programming(limit)

        if dp_list[-1] % DIVISIBLE_LIMIT == 0:
            print("found")
            answer = limit
            divisible = True
        
    return answer




    # # we don't know how many n coins, aka what is the limit?
    # # it needs to be a while loop

    # # initiate dp list
    # dp_list = [1]

    # # final condition
    # divisible = False

    # # initiate coins (n) and amount

    # # start the while loop
    # while not divisible:

    #     # append new element to dp_list
    #     dp_list.append(0)

    #     # interior loop for amount
    #     for amount in range()

    #     # check for divisibility of the added element
    #     if 

    #     # increment coins


coin_partitions()