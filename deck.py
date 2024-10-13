import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        dic = {'S':13, 'H':26, 'D':39, 'C':52}
        for key, value in dic.values():
            if self._card_number < value:
                return key

        

    def get_value(self):
        return self._card_number % 13

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return str(self.get_value())+self.get_suit()

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        pass


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        pass


card = Card(1)
print(card.get_suit())
# deck = Deck()
# deck.shuffle_deck()
# for _ in range(deck.length()):
#     card = deck.take_top_card()
#     print(card.get_long_name())