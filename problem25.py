'''
1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1.

Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_{10} = 55
F_{11} = 89
F_{12} = 144

The 12th term, F_{12}, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

def fibo_index(digits=1000):

    # establish the start of fibonacci
    fibonacci = [1, 1]
    index = False
    i = 2 # current index

    # loop
    while not index:

        # add a new member to sequence
        n = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(n)
        i += 1

        # check number of digits in the member
        string = str(n)

        # if equal to digits, turn index to its index in fibonacci
        if len(string) >= int(digits):

            index = i

    return index

print("Answer to problem 25: ", fibo_index())
