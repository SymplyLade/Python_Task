# Simple Interest Calculator

# Function to calculate simple interest
def calculate_interest(P, R, T):
    return (P * R * T) / 100

# Take inputs from the user
P = float(input("Enter principal amount: "))  # Principal
R = float(input("Enter annual interest rate (in %): "))  # Rate
T = float(input("Enter time period (in years): "))  # Time

# Calculate simple interest
SI = calculate_interest(P, R, T)

# Display the result, rounded to 2 decimal places
print(f"Simple Interest: N{SI:.2f}")