'''
Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n to n/2 (n is even)
n to 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 to 40 to 20 to 10 to 5 to 16 to 8 to 4 to 2 to 1.

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def longest_chain(limit=14):
    
    max_steps = 0
    answer = False

    # create a for loop for all the numbers below million
    for i in range(1, limit):

        current_start = int(i)
        current_steps = [current_start]
        current_num = int(current_start)

        # create a for loop (or while loop? while the current_number != 1)
        while current_num != 1:

            # if the number is even
            if current_num % 2 == 0:
                current_num = int(current_num / 2)

            # if the number is odd
            elif current_num % 2 != 0:
                current_num = int((current_num * 3) + 1)

            # increment current_steps
            current_steps.append(current_num)
        
        # if current_steps > max_steps
        if len(current_steps) > max_steps:
            
            max_steps = len(current_steps)
        
            # assign answer to current_start
            answer = current_start
    

    if answer:
        return answer
    
    return "The function did not work"

print("Answer to problem 14: ", longest_chain(1000000))