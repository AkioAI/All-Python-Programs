import random
def low_high():
    low=int(input("Enter a low number: "))
    high=int(input("Enter a high number: "))
    comp_num=random.randrange(low,high)
    return comp_num
def think():
    print("I am thinking of the number...!")
    num=int(input("Guess the number i am thinking of...!: "))
    return num
def main1(comp_num,num):
    temp=True
    while temp==True:
        if comp_num==num:
            print("Correct you win")
            break
            temp==False
        elif comp_num >  num:
          num=int(input("Too low try again..! : "))
        else:
          num=int(input("Too high try again..! : "))

def main2():
    comp_num=low_high()
    num=think()
    main1(comp_num,num)

main2()