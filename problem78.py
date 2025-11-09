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

COINS = 5
DIVISIBLE_LIMIT = 10**6

def coin_partitions(coins=COINS):

    print("hello coins")

    # divisible by 1 million


# copy def from problem76
def dynamic_programming(limit=LIMIT):
    ''' dynamic programming approach to computing partitions '''

    # dynamic programming list
    dp_list = [0] * (limit + 1)
    dp_list[0] = 1

    print(dp_list)

    for k in range(1, limit + 1):

        for j in range(k, limit + 1):
            # nested loops with indices

            dp_list[j] += dp_list[j-k]
            print("dp list now is ", dp_list)
    
    print(dp_list)

    return (dp_list[limit] - 1)



