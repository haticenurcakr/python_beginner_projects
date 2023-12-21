
import random
from art import logo
import os



def deal_card():
  """return a random card from the deck"""""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards)==21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards)>21: 
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  """bu fonksiyon kart listesi alacak ve bu kartlarda hesaplanan puan listesini döndürücek"""
 
def compare(user_score ,computer_score):
  # conmpare 2 değeri karşılaştıracaktır
  if user_score == computer_score:
    return "draw"
  elif computer_score == 0:
    return "You went over.You lose"
  elif user_score == 0:
    return "win with over. You lose"
  elif user_score > 21 :
    return "you went over. you lose"
  elif computer_score > 21:
    return "opponent went over . you win"
  elif user_score > computer_score :
    return "you win"
  else:
    return "you lose"      
      
def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2): # burdaki "_" özel bir değişkene ihtiyacımız olmadığını belirtmek için kullanılır. 
    user_cards.append(deal_card()) 
    computer_cards.append(deal_card())
    #append kullanmalıyız çünkü bu şekilde döngü sonunda eklenen kartları ekrana yazdırmak için kullanılır.  

  while not is_game_over:

    user_score= calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}") 
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal=input('Type "y" to get another card, type "n" to pass:')
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
                  
 
  while computer_score != 0 and computer_score < 17 :
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print ( f"  your final hand:{user_cards}, final score: {user_score}")
  print(f"  computer's final hand:{computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))
  

def clear_console():
    if os.name == 'nt':  # oyunu her çalıştırdığımızda temizlemek için sisteme göre oluşturduk
        os.system('cls')
    else:
        os.system('clear')


while input("do you want to play a game of  blackjack? type 'y' or 'n'" ) == "y" :
  clear_console()
  play_game()