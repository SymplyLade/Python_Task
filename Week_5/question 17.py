import csv
from datetime import datetime
FILENAME = "expenses.csv"
# Save expense to CSV
def save_expense(date, category, amount, description):
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
# Load expenses from CSV
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses
# Show expense report

        # Category totalscategory_totals = {}
    monthly_totals = {}
    for date, category, amount, desc in expenses:
        amount = float(amount)
        total += amount
        # Category totals
        category_totals[category] = category_totals.get(category, 0) + amount
        # Monthly totals
        month = date[:7]  # e.g. "2025-09"
        monthly_totals[month] = monthly_totals.get(month, 0) + amount
    print("\n=== Expense Report ===")
    print(f"Total Spending: ₦{total:.2f}")
    print("\n--- By Category ---")
    for cat, amt in category_totals.items():
        print(f"{cat}: ₦{amt:.2f}")
    print("\n--- By Month ---")
    for m, amt in monthly_totals.items():
        print(f"{m}: ₦{amt:.2f}")
 
# Main program
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Report")
    print("3. Exit")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter category (Food, Transport, etc.): ").title()
        amount = input("Enter amount: ")
        desc = input("Enter description: ")
        save_expense(date, category, amount, desc)
        print("Expense added successfully!")
    elif choice == "2":
        show_report()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
