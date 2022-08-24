from art import logo
from random import randint
import os

def clear():
  if(os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')

def make_a_guess(number):
  guess = int(input("Make your guess: "))
  if guess == number:
    return "win"
  elif guess > number:
    print("Too high")
  elif guess < number:
    print("Too low")
    
def guess_the_number():
  print(logo)
  print("Welcome to the guessing game!\nI'm thinking of a number between 1 and 100.")
  difficulty = input(f"Choose a difficulty. (Easy or hard)\n") 
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5
  number = randint(1, 100)
  while lives != 0:
    print(f"You have {lives} attempts to guess the number.")
    result = make_a_guess(number)
    lives -=1
    if result == "win":
      break
  if result == None:
    print("You've lost all your lives :(")
  elif result == "win":
    print("You've guessed right!")
   

play = input("Do you want to play? (y/n)\n")
while play == "y":
  guess_the_number()
  play = input(f"\n\nDo you want to play again? (y/n)\n")
  clear()
