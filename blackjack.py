from deck import Deck
from hand import Hand

chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to shuffle again or press 'q' to leave."

def intro():
  statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
  Dealer hits until she reaches 17. Aces count as 1 or 11.
  Card output goes a letter followed by number of the face notation'''
  print (statement)


def make_bet():
  global bet
  bet = 0
  
  print('What amount of chips you like to bet? (enter whole integer please)')
  
  while bet == 0:
    bet_comp = input()
    bet_comp = int(bet_comp)
    
    if bet_comp >= 1 and bet_comp <= chip_pool:
      bet = bet_comp
    else:
      print('Invalid bet. You have only '+ str(chip_pool) + ' chips remaining.')

def deal_cards():
  global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
  
  deck = Deck()
  deck.shuffle()
  
  make_bet()
  
  player_hand = Hand()
  dealer_hand = Hand()
  
  #2 cards to Player
  player_hand.card_add(deck.deal())
  player_hand.card_add(deck.deal())
  
  #2 cards to Dealer
  dealer_hand.card_add(deck.deal())
  dealer_hand.card_add(deck.deal())
  
  result = "Hit or stand? Press 'h' or 's':"
  
  playing = True
  game_step()

def hit():
  global playing, chip_pool, deck, player_hand, dealer_hand, result, bet
  
  if playing:
    if player_hand.calc_val() <= 21:
      player_hand.card_add(deck.deal())
    print('Player hand is %s' %player_hand)
    
    if player_hand.calc_val() > 21:
      result = 'Busted!' + restart_phrase
      chip_pool -= bet
      playing = False
        
  else:
    result = "Sorry, can't hit!" + restart_phrase
      
  game_step()

def stand():
  global playing, chip_pool, deck, player_hand, dealer_hand, result, bet
  
  if playing == False:
    if player_hand.calc_val() > 0:
      result = "Sorry, you can't stand!"
          
  else:
    while dealer_hand.calc_val() < 17:
      dealer_hand.card_add(deck.deal())
          
    if dealer_hand.calc_val() > 21:
      result = 'Dealer Busts! You Win!' + restart_phrase
      chip_pool += bet
      playing = False
        
    elif dealer_hand.calc_val() < player_hand.calc_val():
      result = 'You bet the dealer! You win!' + restart_phrase
      playing = False
        
    else:
      result = 'Dealer Wins!' + restart_phrase
      chip_pool -= bet
      playing = False
  
  game_step()

def game_step():
  print('')
  print('Player hand is: ')
  player_hand.draw(hidden = False)
  print(' Player hand total is: ' + str(player_hand.calc_val()))
  
  print('')
  print('Dealer hand is: ')
  dealer_hand.draw(hidden = True)
  print(' Dealer hand total is: ' + str(dealer_hand.calc_val()))
  
  if playing == False:
      print('Chip total: ' + str(chip_pool))
      
  print(result)
  
  player_input()

def game_exit():
  print('Thanks for playing!')
  exit()

def player_input():
  plin = input().lower()
  
  if plin == 'h':
    hit()
  elif plin == 's':
    stand()
  elif plin == 'd':
    deal_cards()
  elif plin == 'q':
    game_exit()
  else:
    print('Invalid input... Enter h, s, d, or q: ')
    player_input()