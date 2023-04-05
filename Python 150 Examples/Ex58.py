import random as rd
score=0
while score==0:
    for i in range(1,10):
        num1=rd.randint(1,50)
        num2=rd.randint(1,50)
        correct=num1+num2
        print(num1," + ",num2," =")
        answer=int(input("your answer: "))
        if answer==correct:
            print("your answer is correct!")
            score+=1
        print("you scored", score ,"out of 5")
        print("Original answer: ",correct)

