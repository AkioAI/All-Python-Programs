# Banker Roulette
import random
names = input("Enter four names").split(",")
print(names)
name_length = len(names)
random_choice = random.randint(0,name_length-1)
print(f"{names[random_choice]} is going to buy meal today.")
