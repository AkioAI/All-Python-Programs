# Pizza order Exercise

print("Welcome to the Python pizza Delivery!")
size = input("What size do you want? S,M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == 'S' and add_pepperoni == 'Y':
    bill += 15
    bill += 2
elif size == 'S' and add_pepperoni == 'N':
    bill += 15
if (size == 'M' or size == 'L') and add_pepperoni == 'Y':
    if size == 'M' and add_pepperoni == 'Y':
        bill += 20
        bill += 3
    elif size == 'L' and add_pepperoni == 'Y':
        bill += 25
        bill += 3
if (size == 'M' or size == 'L') and add_pepperoni == 'N':
    if size == 'M' and add_pepperoni == 'Y':
        bill += 20
    elif size == 'L' and add_pepperoni == 'Y':
        bill += 25
if extra_cheese == 'Y':
    bill += 1
else:
    pass
print(f"your final bill is {bill}$")
