# #Creating and manipulating strings.
# # - upper()
# # - lower()
# # - title()
# # - strip()
# #  - replace()
# #  - capitalize()
# #  - swapcase()
# #  - strip()
# # - lstrip()
# # - rstrip()
# # - split()
# # - rsplit()
# # - splitlines()
# #  - join()
# # - replace()
# # - center()
# #  - ljust()
# # - rjust()
# #  - zfill()
# # - isalpha()
# # - isdigit()
# # - isalnum()
# # - isspace()
# # - islower()
# # - isupper() 
# #  - istitle()


# # Upper ()
# # Converts all characters in the string to uppercase
# #name = "Ada Balogun"
# print(name.upper())

# # Lower()
# # converts all characters in the string to lowercase. 
# sentence = "Python Is Amazing"
# print(sentence.lower())

# # strip()
# # Removes whitespace (or specified characters)from both ends of the string 
# text = "     Abuja    "
# print(text.strip())


# # Replace occurences of a substring with another substring
# message = " I love Java"
# print(message.replace("Java", "Python"))

# # Swapcase()
# # Switches lowercases to uppercase and vice versa
# text = "Hello ABEOKUTA"
# print(text.swapcase())

# # lstrip()
# # Removes whitespace (or specified characters)from the left sideb only
# text = "         Nigeria"
# print(text.lstrip())

# # Split()
# # Splits a string into a list using a separator (default is space)
# fruits = "mango orange banana"
# print(fruits.split())

# # rsplit()
# # Splits a string into a list from the right side
# text = "one,two,three,four"
# print(text.rsplit(",", 2))

# # splitlines()
# # splits a string into a list at each newline(\n)
# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())

# # Join()
# # Joins a list of strings into one string with a specified separator
# #words = ["I","love", "Python"]
# #print(" ".join(words))

# # Center()
# # Centers the string within a specified width,padding with spaces pr characters
# #text = "Python"
# #print(text.center(20, "-"))

# #ljust()
# # Left-aligns the string within a specified width,padding wihth spaces or character
# #text = "Python"
# #print(text.ljust(10, "*"))

# # rjust()
# # Right-aligns the string within a specified width,padding with spaces or characters
# text = "python"
# print(text.rjust(10, "*"))

# # zfill()
# # Pads a numeric string on the left with zeros until it reaches a given length
#num = "42"
#print(num.zfill(5))

# isalpha()
# Checks if the string contains only letters
#print("Lagos".isalpha())  # True
#print("Lagos123".isalpha())  # False

# isdigit()
# Checks if the string contains only digits
#print("12345".isdigit())  # True
#print("123a".isdigit())   # False

# isalnum()
# Checks if the string contains onlyn letters and digits
print("Python3".isalnum())   # True
print("Python 3".isalnum())  # False