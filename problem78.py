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

def coin_partitions(coins=COINS):

    print("hello coins")

    print(dynamic_programming(coins))




coin_partitions()