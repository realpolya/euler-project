'''
Powerful Digit Counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, 
the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

'''

def powerful_digit_counts():

    count = 0

    for num in range(1, 100):
        for n in range(2, 200):
            # print("for exponent", n, "number of digis", len(str(5 ** n)))
            result = num ** n
            if len(str(result)) == n:
                print("for num", num, "for exponent", n, "number of digis", len(str(result)), "result is:", result)
                count += 1
    
    return count
    
print(powerful_digit_counts())