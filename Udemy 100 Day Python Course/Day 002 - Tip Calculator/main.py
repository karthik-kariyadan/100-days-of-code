print("Welcome to the tip calculator!")

bill = float(input("Enter the total bill: £"))
tip = float(input("Enter your tip as a percentage: ").strip("%"))
people = int(input("Enter the number of people to split the bill between: "))

bill_after_tip = bill * (1 + tip/100)
bill_per_person = bill_after_tip / people
bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: £{bill_per_person}")
