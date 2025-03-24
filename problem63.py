'''
Powerful Digit Counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, 
the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

'''


def powerful_digit_counts():

    distinct_integers = set()

    for num in range(1, 100):
        for n in range(1, 25):
            result = num ** n
            if len(str(result)) == n:
                distinct_integers.add(result)
    
    return len(distinct_integers)
   

print("Answer to problem 63: ", powerful_digit_counts())