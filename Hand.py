from Card import values


class Hand:

    def __init__(self):
        self.cards = []  # Start with an empty list
        self.value = 0  # Start with zero value
        self.aces = 0  # Keep track of aces

    def add_card(self, card):
        # Add card to the cards list
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If a hand's value exceeds 21 but it contains an Ace, reduce the Ace's value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



