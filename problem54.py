'''
Poker Hands

In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

- High Card: Highest value card.
- One Pair: Two cards of the same value.
- Two Pairs: Two different pairs.
- Three of a Kind: Three cards of the same value.
- Straight: All cards are consecutive values.
- Flush: All cards of the same suit.
- Full House: Three of a kind and a pair.
- Four of a Kind: Four cards of the same value.
- Straight Flush: All cards are consecutive values of same suit.
- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the 
highest value wins; for example, a pair of eights beats a pair of fives 
(see example 1 below). But if two ranks tie, for example, 
both players have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest cards are compared, 
and so on.
Consider the following five hands dealt to two players:
H - Hearts, C - Clubs, S - Spades, D - Diamonds

Hand   Player 1                                            Player 2                                              Winner
1      5H 5C 6S 7S KD(Pair of Fives)                       2C 3S 8S 8D TD(Pair of Eights)                       Player 2
2      5D 8C 9S JS AC(Highest card Ace)                    2C 5C 7D 8S QH(Highest card Queen)                   Player 1
3      2D 9C AS AH AC(Three Aces)                          3D 6D 7D TD QD(Flush  with Diamonds)                 Player 2
4      4D 6S 9H QH QC(Pair of Queens, Highest card Nine)   3D 6D 7H QD QS(Pair of Queens, Highest card Seven)   Player 1
5      2H 2D 4C 4D 4S(Full House, With Three Fours)        3C 3D 3S 9S 9D(Full House, with Three Threes)        Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

'''

from extras.poker54 import CARDS

# separate cards by line, then by space to see all of the combinations

class Poker():

    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, hand1, hand2):
        self.hand1 = hand1.split() # list format
        self.hand2 = hand2.split() # list format
        self.winner = False
        self.combo1 = self.identify_combo(1)
        # self.combo2 = self.identify_combo(2)
    

    def is_royal_flush(self, combo):
        '''Ten, Jack, Queen, King, Ace, in same suit. T J Q K A + same letter'''

        necessary = sorted(["T", "J", "Q", "K", "A"])
        values = []

        for char in combo:
            values.append(char[0])

        return sorted(values) == necessary


    def is_straight(self, combo):
        '''Are all cards are consecutive values?'''

        values = []
        for char in combo:
            values.append(char[0])
        sorted_values = sorted(values, key=lambda x: self.__class__.cards.index(x))

        if "".join(sorted_values) == "A2345": # special case
            return True

        return "".join(sorted_values) in "".join(self.__class__.cards)


    def is_four_kind(self, combo):
        '''Is there four cards of the same value?'''
        values_count = {}
        for char in combo:
            if len(values_count) > 2:
                return False
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1
                if values_count[char[0]] == 4:
                    return True
        return False

    def is_full_house(self, combo):
        '''Full House: Three of a kind and a pair.'''
        values_count = {}
        three = False
        pair = False

        for char in combo:
            if len(values_count) > 2:
                return False
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1

        for key, value in values_count.items():
            if value == 2:
                pair = True
            elif value == 3:
                three = True
        
        return (three and pair)
    
    def is_three_kind(self, combo):
        '''Three of a Kind: Three cards of the same value.'''

        values_count = {}
        for char in combo:
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1
                if values_count[char[0]] == 3:
                    return True
        return False
    
    def is_two_pairs(self, combo):
        '''Two Pairs: Two different pairs.'''

        values_count = {}
        pair1 = False
        pair2 = False

        for char in combo:
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1

        for key, value in values_count.items():
            if pair1 == True and value == 2:
                pair2 = True
            elif value == 2:
                pair1 = True
        
        return (pair1 and pair2)

    def is_one_pair(self, combo):
        '''Two cards of the same value.'''

        values_count = {}
        for char in combo:
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1
                if values_count[char[0]] == 2:
                    return True
        return False

    def highest_value(self, combo1, combo2):
        '''Compares two combos to see which one has the highest value card'''


    def is_same_suit(self, combo):
        '''Are all cards of the same suit? Flush'''

        first = True
        for char in combo:
            if first:
                first_suit = char[1]
                first = False
            if char[1] != first_suit:
                return False
        
        return True

    
    def identify_combo(self, number):

        # only do flushes if same suit check has passed

        if number == 1:

            if self.is_same_suit(self.hand1):
                '''all cards of the same suit'''
                if self.is_royal_flush(self.hand1):
                    return "royal_flush"
                if self.is_straight(self.hand1):
                    return "straight_flush"
                return "flush"

            if self.is_four_kind(self.hand1):
                return "four_kind"
            if self.is_full_house(self.hand1):
                return "full_house"
            if self.is_straight(self.hand1):
                return "straight"


            




first_game = Poker("5H 5C 6S 7S KD", "5D 8C 9S JS AC")
second_game = Poker("QH KH JH TH 3H", "5D 8C 9S JS AC")
third_game = Poker("QH QH QH TH QH", "5D 8C 9S JS AC")
third_game = Poker("QH QH TH TH QH", "5D 8C 9S JS AC")
# first_game.is_royal_flush()

# separate by line
# first 5 are first player, second 5 are second player