# The Game of Rock Paper Scissors
import random

moves = ["rock", "paper", "scissors"]

# Player Move
your_move = input("Please choose Rock (r) or Paper (p) or Scissors (s): ")

if your_move == "r":
    your_move = "rock"
    print(f"\nYour move: {your_move.title()}")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif your_move == "p":
    your_move = "paper"
    print(f"\nYour move: {your_move.title()}")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif your_move == "s":
    your_move = "scissors"
    print(f"\nYour move: {your_move.title()}")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Please select correct option.")

# Computer Move
pick = random.randint(0,2)
comp_move = moves[pick]

if comp_move == "rock":
    print(f"Computer Move: {comp_move.title()}")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif comp_move == "paper":
    print(f"Computer Move: {comp_move.title()}")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif comp_move == "scissors":
    print(f"Computer Move: {comp_move.title()}")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Compare Moves and Decide a Winner

if your_move == "rock":
    if comp_move == "rock":
        print(f"This game is a draw.\n")
    elif comp_move == "paper":
        print(f"Computer Wins!\n")
    elif comp_move == "scissors":
        print(f"Yay! You Win!\n")
elif your_move == "paper":
    if comp_move == "rock":
        print(f"Yay! You Win!\n")
    elif comp_move == "paper":
        print(f"This game is a draw.\n")
    elif comp_move == "scissors":
        print(f"Computer Wins!\n")
else:
    if comp_move == "rock":
        print(f"Computer Wins!\n")
    elif comp_move == "paper":
        print(f"Yay! You Win!\n")
    elif comp_move == "scissors":
        print(f"This game is a draw.\n")
