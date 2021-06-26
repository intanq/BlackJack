from Deck import Deck
from Hand import Hand
from Chips import Chips
from Player import Player

playing = True


def show_some(player, dealer):
    print("\nDealer's hand: ")
    print("<card hidden>")
    print('', (dealer.get_cards()[1]))
    print("\nPlayer's hand: ", *player.get_cards(), sep="\n")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.get_cards(), sep='\n ')
    print("Dealer's Hand =", dealer.hand.value)
    print("\nPlayer's Hand:", *player.get_cards(), sep='\n ')
    print("Player's Hand =", player.hand.value)


# FUNCTIONS TO HANDLE END OF GAME SCENARIOS


def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")


# FUNCTION TO PROMPT THE USER WHETHER THEY WANT TO HIT OR STAND

def hit_or_stand(deck, player):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' for Hit OR 's' for Stand. ")

        if x[0].lower() == 'h':
            player.hit(deck)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


# THE GAME

while True:

    print('Welcome to BlackJack! Get as close to 21 as you can without going over it!\n'
          'Dealer hits until he/she reaches 17. Aces count as 1 or 11.')

    # Create and shuffle the deck

    deck = Deck()
    deck.shuffle()

    # Create player object (Player class)
    player = Player('Player', Hand(), Chips())
    player_hand = player.hand
    player_chips = player.chips
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Create dealer object (Player class)
    dealer = Player('Dealer', Hand(), Chips())
    dealer_hand = dealer.hand
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Prompt the player to take their bet
    player.take_bet()

    # Show cards but keep one dealer card being hidden
    show_some(player, dealer)

    while playing:
        # Ask the player whether they want to hit or stand
        hit_or_stand(deck, player)

        show_some(player, dealer)

        # Check whether the player's hand exceeds 21
        if player.hand.value > 21:
            player_busts(player_chips)
            break

    # If player has not busted, play Dealer's hand until Dealer reaches value of 17
    if player.hand.value <= 21:
        while dealer.hand.value < 17:
            dealer.hit(deck)

        # Show all cards
        show_all(player, dealer)

        # Run different scenarios of winning
        if dealer.hand.value > 21:
            dealer_busts(player_chips)

        elif dealer.hand.value > player.hand.value:
            dealer_wins(player_chips)

        elif dealer.hand.value < player.hand.value:
            player_wins(player_chips)

        else:
            push()

    # Inform player of their chips total
    print(f"\nYour chips: {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break