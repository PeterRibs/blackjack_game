from deck import Deck
from hand import Hand
from blackjack import intro
from blackjack import deal_cards

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()
deal_cards()