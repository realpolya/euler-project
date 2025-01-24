'''
Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317.
Find the last ten digits of the series, 
1^1 + 2^2 + 3^3 + ... + 1000^{1000}.

'''

def self_powers(limit):

    ten_digits = ''
    sum = 0

    for n in range(1, limit + 1):

        sum += n ** n

    sum_list = list(str(sum))

    for i in range(-10, 0, 1):

        ten_digits += sum_list[i]
    
    return ten_digits



print("Answer to problem 48: ", self_powers(1000))