# Nested if else
print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoster")
    if age <= 12:
        print("Please pay 350₹")
    elif age <=18:
        print("Please pay 490₹.")
    else:
        print("Please pay 840₹.")
else:
    print("Sorry, you have to grow taller before you can ride. ")
