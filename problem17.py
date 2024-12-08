'''
Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''

from num2words import num2words

def write_nums(limit):
    # empty list of words
    words = []
    sum = 0

    # for loop
    for i in range (1, int(limit) + 1):
    
        # add words into the array
        word = num2words(i)
        words.append(word)

        # split the string
        chars = list(word)

        # filter list
        filtered_chars = [char for char in chars if not ("," in char or '-' in char or ' ' in char)]
        print("filtered chars are ", filtered_chars)

        # calculate the sum of the letters, exclude commas, spaces and hyphens
        sum += len(filtered_chars)

    # return the sum
    return sum

print(write_nums(5))
print(write_nums(1000))