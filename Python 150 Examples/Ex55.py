import random as rd
num=rd.randrange(1,5)
choose=int(input("Pick a number: "))
if choose==num:
    print("Well Done!")
elif choose>5:
    print("Too High.")
elif choose<1:
    print("Too Low.")
choose2=int(input("Pick a second number: "))
if choose2==num:
    print("Correct!")
else:
    print("You Lose!")