# Mad Libs Game

# Welcome message
print("Welcome to Mad Libs!")

# Collect words from the user
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

# Create the Mad Libs story using f-string
story = f"Once upon a time, a {adjective} {noun} {verb} through the {place}. It was an unforgettable journey!"

# Display the final story
print("\nHere is your Mad Libs story:")
print(story)


