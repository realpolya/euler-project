'''
Arranged Probability

If a box contains twenty-one coloured discs, composed of 
fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21) * (14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance 
of taking two blue discs at random, is a box containing eighty-five blue 
discs and thirty-five red discs.

By finding the first arrangement to contain over 10^{12} = 1,000,000,000,000 
discs in total, determine the number of blue discs that the box would contain.

'''

def find_probability(item_quantity, total_quantity, repeat_times=2):

    probability = 1

    for _ in range(repeat_times):
        probability *= item_quantity / total_quantity
        item_quantity -= 1
        total_quantity -= 1

    return probability



def arranged_probability():

    # unknown number of reds, unknown number of blues

    # find first instance first

    # nested loops of blue and red, until the answer is found

    answer = False
    blue = 1

    while not answer:


