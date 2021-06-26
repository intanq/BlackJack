class Player:

    def __init__(self, name, hand, chips):
        self.name = name
        self.hand = hand
        self.chips = chips

    def get_cards(self):
        return self.hand.cards

    def take_bet(self):

        while True:
            try:
                self.chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if self.chips.bet > self.chips.total:
                    print(f"Sorry, your bet cannot exceed {self.chips.total}")
                else:
                    break

    def hit(self, deck):
        # This function will be called anytime the Player wants to hit OR a Dealer's hand is less than 17
        self.hand.add_card(deck.deal())
        self.hand.adjust_for_ace()






