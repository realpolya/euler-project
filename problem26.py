'''
Reciprocal Cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions 
with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

TODO: fix the solution below

'''

def find_cycle(limit=10):

    repeat_floats = []
    winner = False
    max_len = 0

    # for loop
    for n in range(2, limit+1):

        # calculate float
        current = 1 / int(n)

        # in recurring cycles remainders in decimal start to repeat
        quotient = "0."

        infinite = True
        first = True
        remainders = set()
        remainder = 1
        len = 0

        while remainder not in remainders and infinite:

            # print("1.remainder is ", remainder, "n is ", n)

            digit = (10 * remainder) // n
            quotient += str(digit)
            len += 1

            # if remainder is 0, skip iteration
            if remainder == 0:
                # print("reached 0")
                infinite = False
                break

            # add current remainder
            if first:
                first = False
            else:
                remainders.add(remainder)
                # print("2.remainders are ", remainders)

            # calculate the next remainder
            remainder = ((remainder * 10) % n)

            # print("3.new remainder is ", remainder)
        
            # if remainder in remainders:
            #     print("4.STOP: remainders are ", remainders)

            if len > max_len:
                max_len = len
                winner = n

        if infinite:
            repeat_floats.append(quotient)

        # print("for 1/", n, "the quotient is ", quotient)
        
        # create a set of remainders

        # while remainder keeps changing, keep going adding numbers to the sequence
    
    
    return winner
    
print("Answer to problem 26: ", find_cycle(1000))
    

