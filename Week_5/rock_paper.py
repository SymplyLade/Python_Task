# Rock, Paper, Scissors Game

import random

# Define possible choices
choices = ["rock", "paper", "scissors"]

# Ask user to make a choice
user_choice = input("Enter rock, paper, or scissors: ").lower().strip()

# Validate user input
if user_choice not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")):
        print("You win!")
    else:
        print("Computer wins!")