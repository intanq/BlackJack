import random
from Card import suits
from Card import ranks
from Card import Card


class Deck:

    def __init__(self):
        # Instantiate all the cards
        self.deck = []
        for suit in suits:
            for rank in ranks:
                newCard = Card(suit, rank)
                self.deck.append(newCard)

    def __str__(self):
        return '\n'.join(str(e) for e in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()