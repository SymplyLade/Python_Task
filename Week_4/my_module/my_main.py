# my_module/main.py
import my_first
import my_second

# lets use the functions in the first.py file
print("=== Math Functions ===")
print("5 + 3 =", my_first.add(5, 3))
print("10 - 4 =", my_first.subtract(10, 4))
print("6 * 7 =", my_first.multiply(6, 7))
print("20 / 5 =", my_first.divide(20, 5))

# # Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))