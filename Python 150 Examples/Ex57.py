import random as rd
num=rd.randint(1,10)
correct=False
while correct==False:
    choose=int(input("Enter a number: "))
    if choose == num:
        print("True")
    elif choose>10:
        print("Too High")
    else:
        choose<1
        print("Too Low")
