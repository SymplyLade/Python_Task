# Single quotes
name = 'Ada'
print(name)

# Double  quotes
greeting ="Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''once upon a time,
there  was a coder named Ada.'''  # when doubled quotes was used,error occurs without allowing the sentences to bring its new line
print(story)

# Strings with numbers and symbols 
passwords = "p@ssw0rd123"
print(passwords)

# String operations
# Indexing
word = "python"
print(word[0])   # P
print(word[-1])  # n

# Slicing 
word = "Python"
print(word[0:4])   # Pyth
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::2])   # Pto
print(word[::-1])

# String Concatenation & Repetition
# Concatenation
a ="Hello"
b = "World"
print(a + " " + b)  # Hello World

# Repetition
word = "Hi! "
print(word * 3) # Hi! Hi! Hi!

# String Searching & Checking
# Membership
text = "python programming"
print("Python" in text)   #True 
print("Java" not in text)  #True

#find()  / rfind()
text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  #7

#index() / rindex()
#. (Like find() but raises an error if not found)
text = "Hello World"
print(text.index("World"))   #6

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))   #True
print(filename.endswith(".csv"))      #True

