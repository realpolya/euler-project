'''
Passcode Derivation

A common security method used for online 
banking is to ask the user for three random characters 
from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; 
the expected reply would be: 317.

The text file contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest 
possible secret passcode of unknown length.

'''

from extras.problem79_extra import ATTEMPTS

def derive_passcode():
    # the numbers are always in order

    # initiate a passcode variable
    passcode = ''

    count = 0 # temp count

    # loop through attempts
    for attempt in ATTEMPTS:

        digits = str(attempt)

        # loop through digits
        for digit in digits:

            # if digits are not seen before, concatenate
            if str(digit) not in passcode:

                passcode += str(digit)
        
        count += 1

        if count > 2:
            break

    # follow the order of digits until something does not click

    print(passcode)




# print(ATTEMPTS)

derive_passcode()