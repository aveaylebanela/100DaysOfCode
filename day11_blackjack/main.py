from random import choice
from art import logo
import os

def clear():
  if(os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')

def get_a_card(ones_cards):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  ones_cards.append(choice(cards))

def calculate_a_score(cards):
  if sum(cards) == 21:
    return 0
  else:
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(0)
    return sum(cards)

def compare(user_score, computer_score):
  winner = ''
  if computer_score == 0 and user_score == 0:
    winner = "draw"
  elif user_score == 0 or computer_score > 21:
    winner = "user"
  elif user_score > 21 or computer_score == 0:
    winner = "computer"
  return winner

def anounce_status(user_cards, computer_cards):
  return f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}"

def blackjack():
  computer_cards = []
  user_cards = []
  winner = ''
  more = 'n'

  for i in range(2):
    get_a_card(user_cards)
    get_a_card(computer_cards)

  print(anounce_status(user_cards, computer_cards))
  winner = (compare(calculate_a_score(user_cards),       calculate_a_score(computer_cards)))

  if compare(calculate_a_score(user_cards), calculate_a_score(computer_cards)) == "":
    more = input("One more card? (y/n) \n")
    while more == "y":
      get_a_card(user_cards)
      print(anounce_status(user_cards, computer_cards))
      if compare(calculate_a_score(user_cards), calculate_a_score(computer_cards)) != "":
        winner = compare(calculate_a_score(user_cards), calculate_a_score(computer_cards))
        break
      more = input("One more card? (y/n) \n")

    if more == "n":
      while 21 < calculate_a_score(computer_cards) < 17:
        get_a_card(computer_cards)

  if compare(calculate_a_score(user_cards), calculate_a_score(computer_cards)) == "":
    if calculate_a_score(computer_cards) > calculate_a_score(user_cards):
      winner = "computer"
    elif calculate_a_score(computer_cards) < calculate_a_score(user_cards):
      winner = "user"
    elif calculate_a_score(computer_cards) == calculate_a_score(user_cards):
      winner = "draw"
  if winner == "computer":
    print("You lose")
  elif winner == "user":
    print("You win!")
  elif winner == "draw":
    print("It's a draw!")

play = input(f"Do you want to play? (y/n)\n")
while play == "y":
  clear()
  print(logo)
  blackjack()
  play = input("Do you want to play again? (y/n)\n")
