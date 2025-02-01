'''
Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

def same_digits(x, y):
    '''Do x and y contain the same digits?'''

    x_list = list(str(x))
    y_list = list(str(y))

    if sorted(x_list) == sorted(y_list):
        return True
    
    return False


def find_smallest(multiple_limit):

    answer = False
    n = 10

    while not answer:

        current_solution = True

        for x in range(2, multiple_limit + 1):

            multiple = x * n

            if not same_digits(n, multiple):
                current_solution = False
                break
        
        if current_solution:
            answer = n
        else:
            n += 1
    
    return answer

print("Answer to problem 52: ", find_smallest(6))