
playing = False
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.ace = False
    
  def __str__(self):
    hand_comp = ''
    
    for card in self.cards:
      card_name = card.__str__()
      hand_comp += " " + card_name
        
    return 'The hand has {}'.format(hand_comp)
  
  def card_add(self, card):
    self.cards.append(card)
      
    if card.rank == 'A':
      self.ace = True
    self.value += card_val[card.rank]
      
  def calc_val(self):
    if(self.ace == 'True' and self.value < 12):
      return self.value + 10
    else:
      return self.value
      
  def draw(self, hidden):
    if (hidden == True and playing == True):
      starting_card = 1
    else:
      starting_card = 0
      for x in range(starting_card, len(self.cards)):
        self.cards[x].draw()