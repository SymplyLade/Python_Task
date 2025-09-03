import random

# Generate a random number between 1 and 100, with a step of 5
number = random.randrange(5,100,5)

# Variable to track number of attempts
attempts = 0

# Welcome message
print("Guess the number in multiple of 5s, between 5 and 8")

# Infinite loop until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increase attempt count

    # Provide feedback based on the guess
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        # Correct guess
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  # Exit the loop