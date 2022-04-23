import random
from card import Card

suits = ('H', 'D', 'C', 'S')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

class Deck:
  def __init__(self):
    self.deck=[]
    
    for suit in suits:
      for rank in ranking:
        self.deck.append(Card(suit, rank))
              
  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card

  def __str__(self):
    deck_comp=''
    for card in self.deck:
      deck_comp += " " +card.__str__()

    return 'The deck has ' + deck_comp