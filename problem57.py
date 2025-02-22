'''
Square Root Convergents

It is possible to show that the square root of two can be 
expressed as an infinite continued fraction.
\sqrt 2 = 1 + 1 / {2 + 1 / {2 + 1 / {2+ ...}}}
By expanding this for the first four iterations, we get:
1 + 1 / 2 =  32 = 1.5
1 + 1 / {2 + 1 / 2} = 7 5 = 1.4
1 + 1 / {2 + 1 / {2 + 1 / 2}} = 17 / 12 = 1.41666...
1 + 1 / {2 + 1 / {2 + 1 / {2 + 1 / 2}}} = 41/ 29 = 1.41379...

The next three expansions are  99/70,  239/169, and  577/408, 
but the eighth expansion,  1393/985, is the first example where the 
number of digits in the numerator exceeds the number of digits in the 
denominator.

In the first one-thousand expansions, how many fractions contain a 
numerator with more digits than the denominator?

'''

from fractions import Fraction


def square_root_conv(limit=1000):

    count = 0
    current_fraction = Fraction(1, 2)

    for _ in range(limit):

        # current result

        # evaluate as a fraction

        # count the number of digits for both numerator and denominator

        # if the numerator exceeds denominator, increase count
