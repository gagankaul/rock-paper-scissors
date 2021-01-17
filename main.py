#A simple adaptation of the popular Rock, Paper, Scissors game coded in Python.

#The random module plays a key role in this program so we need to import it first.

import random

#Initialize the variable to check if the user would like to play again.

play_again = 0

#Check for recurring play and enable it using the while loop.

while play_again != "n":
  
  moves = ['rock','paper','scissors']
  
  your_move = input("\nWhat's your move? Rock, Paper, Scissors?\n")
  
  random_pick = random.randint(0,2)
  
  comp_move = moves[random_pick]
  
  if your_move == "r":
    your_move = "rock"
  elif your_move == "p":
    your_move = "paper"
  elif your_move == 's':
    your_move = "scissors"

  print(f"Your awesome pick is {your_move}")
  print(f"The computer picked {comp_move}")  
  
  if your_move == comp_move:
    print("\nIt's a draw! Try again!")
  elif your_move == 'p' and comp_move == 'rock':
    print("\nYou win. You are awesome!")
  elif your_move == 's' and comp_move == 'paper':
    print("\nYou win. You are awesome!")
  elif your_move == 'r' and comp_move == 'scissors':
    print("\nYou win. You are awesome!")
  else:
    print("The mighty computer wins!\n")
    
  play_again = input("\nWould you like to play again (y/n)?\n")