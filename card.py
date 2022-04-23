class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return self.suit + self.rank
  
  def grab_suit(self):
    return self.suit
  
  def grab_rank(self):
    return self.rank
  
  def draw(self):
    print(self.suit + self.rank)