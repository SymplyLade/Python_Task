# String Manipulation:

# - Using string methods like split() and
# - Extracting specific parts of a string

# User Input Handling:

# - Accepting an email address from the user
# - Validating the input format

# Output Formatting:

# - Displaying extracted username and domain clearly
# """
def email_slicer():
    # Get user input
    email = input("Enter your email: ")
    # Validate if input contains '@'
    if '@' not in email:
        print("Invalid email format!")
        return
    # Split email into username and domain
    username, domain = email.split('@')
    # Display extracted username and domain
    print(f"Username: {username}")
    print(f"Domain: {domain}")
if __name__ == "__main__":
    email_slicer()
