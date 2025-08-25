# Defne varaibles with integers
#score =13            # data type int
#name="Lade"         # data types string
#height =6.5          # data type float
#print(f"{name} scored {score} height {height}")

#str()
#float()
#bool()

#age = int(input("Enter your age:"))
#print(f"You will be {age + 1} years old next year.")

# step 1 create a bot welcome text
# step 2 create a list for selection

options = int(input("Choose your option\n1. Recharge\n2. Data\n3. Enquiry\n4. Others\n5. Exit\n Enter option: "))
print(f"Are you sure you want to purchase {options} ")

amount = input("Enter amount\n ₦100\n ₦200\n ₦300\n ₦400\n ₦500\n ₦1000\n: ")
print(f"Are u sure u want to purchase ₦{amount} Recharge card?")

confirmation = input("Enter yes to proceed: ")
print(f"Congratulations, you have successfully purchase {amount} rechage card")