import re
def validate_email(email):
    # Regular expression to validate email format
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None
def email_slicer():
    while True:
        # Get user input
        email = input("Enter your email (or 'quit' to exit): ")
        if email.lower() == 'quit':
            break
        # Validate email format
        if not validate_email(email):
            print("Invalid email format! Please try again.")
            continue
        # Split email into username and domain
        username, domain = email.split('@')
        # Display extracted username and domain
        print(f"Username: {username}")
        print(f"Domain: {domain}\n")
if __name__ == "__main__":
    email_slicer()