while True:
    print("Enter 'x' for exit")
    num=input("Enter the number")
    if num=='x':
        exit()
    else:
        number=int(num)
        if number>0 and number<100:
            if number>0 and number<=50:
                     print("your no. lies between 0-50.\t\t")
            else:
                     print("your no. lies between 51-100.\t\t")
        else:
            print("your no. is above 100.\t\t")

