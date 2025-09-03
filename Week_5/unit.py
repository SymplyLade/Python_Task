# Display menu
print("\nUnit Converter")
print("1. Meters to Kilometers")
print("2. Kilometers to Miles")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Grams to Kilograms")

# Get user choice
choice = input("Enter your choice (1-5): ")

# Get value to convert
value = float(input("Enter the value: "))

# Perform conversion based on user choice
if choice == '1':
    print(f"{value} meters is {meters_to_kilometers(value)} kilometers")
elif choice == '2':
    print(f"{value} kilometers is {kilometers_to_miles(value)} miles")
elif choice == '3':
    print(f"{value} Celsius is {celsius_to_fahrenheit(value)} Fahrenheit")
elif choice == '4':
    print(f"{value} Fahrenheit is {fahrenheit_to_celsius(value)} Celsius")
elif choice == '5':
    print(f"{value} grams is {grams_to_kilograms(value)} kilograms")
else:
    print("Invalid choice! Please enter a number between 1 and 5.")