from art import logo
import os

def clear():
  """clears the console, takes/returns nothing"""
  # posix is os name for linux or mac
  if(os.name == 'posix'):
     os.system('clear')
  # else screen will be cleared for windows
  else:
     os.system('cls')
    
def add(n1, n2):
  """takes two numbers, adds them, returns the result"""
  return n1 + n2

def substract(n1, n2):
  """takes twon numbers, substracts them, returns the result"""
  return n1 - n2

def multiply(n1, n2):
  """takes two numbers, multipies, returns result"""
  return n1 * n2

def divide(n1, n2):
  """takes two numbers, devides, returns result"""
  return n1 / n2

operations = {
  "+":add, 
  "-":substract, 
  "*":multiply, 
  "/": divide
}
