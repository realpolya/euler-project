'''
Coin Sums

In the United Kingdom the currency is made up of pound (£) and 
pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

'''

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sums(coins=COINS, goal=200):

    # how many sum permutations can be completed to get to 200
    results = []

    # recursive function
    def backtrack(start, current_combo, current_sum):

        # base case
        if current_sum == goal:

            # print("found a combo")

            # append the list to results
            results.append(list(current_combo))
            return
        
        # if exceeded the needed sum
        if current_sum > goal:
            # print("exceeded")
            return
        
        for i in range(start, len(coins)):

            # print("current combo is ", current_combo, "current sum is ", current_sum, "coins[i] is ", coins[i])

            # include coins[i] in current combination
            current_combo.append(coins[i])

            # recurse with the updated sum, keep the same index
            backtrack(i, current_combo, current_sum + coins[i])

            # remove the last added number
            current_combo.pop()

    # start the recursive cycle
    backtrack(0, [], 0)

    return len(results)


print("Answer to problem 31: ", coin_sums())
# coin_sums([2, 3, 4], 8)