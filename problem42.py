'''
Coded Triangle Numbers

The n-th term of the sequence of triangle numbers is given by,

t_n = 1/2 * n * (n+1); 
t * 2 = n * (n + 1)
t * 2 = n^2 + n

so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 

For example, the word value for SKY is 19 + 11 + 25 = 55 = t_{10}. 
If the word value is a triangle number then we shall call the 
word a triangle word.

Using words.txt, a 16K text file 
containing nearly two-thousand common English words, 
how many are triangle words?

'''

from extras.words42 import WORDS
from extras.alphabet import ALPHABET


def calculate_value(word, alphabet):

    value = 0

    for char in word:
        value += alphabet[char] 
    
    return value



def coded_triange_numbers(words=WORDS):

    word_count = 0
    max_value = 0
    triangles = []

    for word in words:
        word_value = calculate_value(word, ALPHABET)
        if word_value > max_value:
            max_value = word_value
    
    n = 1
    current_triangle = 0

    while current_triangle < max_value:
        current_triangle = 1/2 * n * (n + 1)
        triangles.append(int(current_triangle))
        n += 1

    for word in words:
        word_value = calculate_value(word, ALPHABET)
        if word_value in triangles:
            word_count += 1

    return word_count


print("Answer to problem 42: ", coded_triange_numbers())