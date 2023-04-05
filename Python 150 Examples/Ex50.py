temp=0
while temp==0:
    num=int(input("Enter a number: "))
    if num<10:
        print("too low")
        print("try again!")
    elif num>20:
        print("too high")
        print("try again!")
    else:
        print("Thank you!")
    break