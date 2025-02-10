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
    combos = [
        "high_card", 
        "one_pair", 
        "two_pairs",
        "three_kind",
        "straight",
        "flush",
        "full_house",
        "four_kind",
        "straight_flush",
        "royal_flush"
    ]

    def __init__(self, hand1, hand2):
        self.hand1 = hand1.split() # list format
        self.hand2 = hand2.split() # list format
        self.combo1 = self.identify_combo(self.hand1)
        self.combo2 = self.identify_combo(self.hand2)
        self.count1 = self.count_values(self.hand1) # dictionary with count
        self.count2 = self.count_values(self.hand2) # dictionary with count
        self.winner = self.identify_winner()
    
    def count_values(self, combo):
        '''Create a dictionary with count.'''

        values_count = {}
        for char in combo:
            if char[0] not in values_count:
                values_count[char[0]] = 1
            elif char[0] in values_count:
                values_count[char[0]] += 1

        return values_count
    
    def identify_winner(self):
        '''Compare the combos'''
        for i, combo in enumerate(self.__class__.combos):
            if combo == self.combo1:
                score1 = i
            if combo == self.combo2:
                score2 = i

        if score1 > score2:
            return "player1"
        elif score1 < score2:
            return "player2"

        return self.deal_with_ties()

    def deal_with_ties(self):
        '''Resolve any tie issues'''
        if self.combo1 in ["one_pair", "two_pairs", "three_kind", "four_kind"]:
            max1 = 0
            max2 = 0
            
            #base case
            if len(combo1) == 0 and len(combo2) == 0:
                return "Tie"
            
            for i, card in enumerate(self.__class__.cards):

                for combo_card in combo1:
                    if combo_card[0] == card and i > max1:
                        max1 = i
                
                for combo_card in combo2:
                    if combo_card[0] == card and i > max2:
                        max2 = i

        winner = self.highest_value()
        if winner == "1":
            return "player1"
        elif winner == "2":
            return "player2"

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

    def highest_value(self, combo1=None, combo2=None):
        '''Compares two combos to see which one has the highest value card'''

        max1 = 0
        max2 = 0

        if combo1 is None and combo2 is None:
            combo1 = list(self.hand1)
            combo2 = list(self.hand2)
        
        #base case
        if len(combo1) == 0 and len(combo2) == 0:
            return "Tie"
        
        for i, card in enumerate(self.__class__.cards):

            for combo_card in combo1:
                if combo_card[0] == card and i > max1:
                    max1 = i
            
            for combo_card in combo2:
                if combo_card[0] == card and i > max2:
                    max2 = i
        
        # print("max for 1 is ", self.__class__.cards[max1], "max for 2 is ", self.__class__.cards[max2])

        if max1 > max2:
            return "1"
        elif max2 > max1:
            return "2"
        elif max1 == max2:
            reduced1 = [card for card in combo1 if self.__class__.cards[max1] not in card]
            reduced2 = [card for card in combo2 if self.__class__.cards[max1] not in card]
            return self.highest_value(reduced1, reduced2)

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
    
    def identify_combo(self, combo):

        # only do flushes if same suit check has passed
        if self.is_same_suit(combo):
            '''all cards of the same suit'''
            if self.is_royal_flush(combo):
                return "royal_flush"
            if self.is_straight(combo):
                return "straight_flush"

            return "flush"

        if self.is_four_kind(combo):
            return "four_kind"
        if self.is_full_house(combo):
            return "full_house"
        if self.is_straight(combo):
            return "straight"
        if self.is_three_kind(combo):
            return "three_kind"
        if self.is_two_pairs(combo):
            return "two_pairs"
        if self.is_one_pair(combo):
            return "one_pair"
        
        return "high_card"
    
    def print_combo(self):
        print("combo for 1 is ", self.combo1)
        print("combo for 2 is ", self.combo2)
        print("winner is ", self.winner)


first_game = Poker("5H 5C 6S 7S KD", "2C 3S 8S 8D TD")
first_game.print_combo()

second_game = Poker("5D 8C 9S JS AC", "2C 5C 7D 8S QH")
second_game.print_combo()

third_game = Poker("2D 9C AS AH AC", "3D 6D 7D TD QD")
third_game.print_combo()

fourth_game = Poker("4D 6S 9H QH QC", "3D 6D 7H QD QS")
fourth_game.print_combo()

fifth_game = Poker("2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D")
fifth_game.print_combo()

# separate by line
# first 5 are first player, second 5 are second player