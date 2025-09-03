from datetime import datetime
def calculate_age(dob):
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    months = today.month - dob.month
    if months < 0:
        months += 12
    days = today.day - dob.day
    if days < 0:
        # Simplification; actual days calculation is more complex due to month lengths
        days += 30  # Approximation
    return age, months, days
def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        age_years, age_months, age_days = calculate_age(dob)
        print(f"Your age is: {age_years} years, {age_months} months, {age_days} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == "__main__":
    main()