'''
Spiral Primes

Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers 
lying along both diagonals are prime; that is, a ratio of 8/13 approximately 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the 
square spiral for which the ratio of primes along both diagonals 
first falls below 10%?

'''

from extras.utils import is_prime


def spiral_primes(percentage=0.1):

    size = 3
    mid = int(size/2)

    r = mid + 1 # start position for r
    i = mid + 1 # start position for i
    n = 1
    current = 2 # number of steps in each direction

    prime_count = 0
    diagonal_count = 1

    ratio = 1

    while ratio > percentage:

        final_step = [current - 1,
        (current * 2) - 1, (current * 3) - 1, (current * 4) - 1]

        for step in range(current * 4):

            if step < current: # up
                n += 1
                r -= 1
            elif step < current * 2: # left
                n += 1
                i -= 1
            elif step < current * 3: # down
                n += 1
                r += 1
            else: # right
                n += 1
                i += 1

            if step in final_step:
                diagonal_count += 1

                if is_prime(n):
                    prime_count += 1
        
        # calculate ratio
        ratio = prime_count / diagonal_count

        if ratio < percentage:
            answer_side = size
        else:
            size += 2

            # spiral ended
            current += 2
            i += 1 # move onto a new spiral
            r += 1 # move onto a new spiral
    
    return answer_side


print("Answer to problem 58: ", spiral_primes())