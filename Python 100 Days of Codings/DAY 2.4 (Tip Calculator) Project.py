# Tip Calculator
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10,12 or 15?" ))
split = int(input("How many people to split the bill?"))
per_tip = tip / 100
new_bill = bill * per_tip
total_bill = bill + new_bill
new_split = total_bill / split
print(f"each person should pay {new_split}")
