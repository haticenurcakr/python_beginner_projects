import random
from game_data import data
from art_2 import logo, vs
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def random_choice_from_list():
    return random.choice(data)

def choose_player():
    return random_choice_from_list(), random_choice_from_list()

def compare(player1, player2):
    return player1['follower_count'] > player2['follower_count']

def user_chose(player1, player2):
    user_answer = input(f"Who has more followers? Type {player1['name']} = A or {player2['name']} = B: ").upper()
    return user_answer == "A" if compare(player1, player2) else user_answer == "B"

def game():
    point = 0
    player1, player2 = choose_player()

    while True:
        print(logo)
        if point > 0:
            print(f"Your score is {point}")
        print(f"Compare A: {player1['name']} ,a {player1['description']} from {player1['country']}")
        print(vs)
        print(f"Compare B: {player2['name']} ,a {player2['description']} from {player2['country']}")

        if user_chose(player1, player2):
            print(f"You are right! {player1['name']} has more followers")
            point += 1
            player1 = player2
            player2 = random_choice_from_list()
            clear_console()
        else:
            clear_console()
            print(logo)
            print(f"Sorry that's wrong! Final score {point}")
            break

while input("Do you want to play a game of higher lower? Type 'y' or 'n': ").lower() == "y":
    clear_console()
    game()
