'''
Names Scores

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?

'''

from extras.names import NAMES
from extras.alphabet import ALPHABET

def names_sum(names=NAMES):

    # sort alphabetically
    ordered_names = sorted(names)

    # initiate sum
    sum = 0

    # loop through names
    for index, name in enumerate(ordered_names):

        # initiate letter score
        letter_total = 0

        # loop thorugh letters:
        for letter in name:

            # update letter score
            letter_total += int(ALPHABET[letter])
        
        # get the place in the sorted list
        place = int(index + 1)

        # multiply to get the name score
        name_score = place * letter_total

        # add to the sum
        sum += name_score

    return sum


print("Answer to problem 22: ", names_sum())