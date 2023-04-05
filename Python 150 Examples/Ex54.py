import random as rd
coin=rd.choice(['h','t'])
guess=input("Enter your choice: (h/t) ")
if guess==coin:
    print("YOU WIN")
else:
    print("BAD LUCK")
if coin=='h':
    print("It was Heads")
else:
    print("It was Tails")
