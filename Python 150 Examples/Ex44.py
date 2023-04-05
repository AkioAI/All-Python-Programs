num=int(input("Enter peoples you want to invite"))
if num<10:
    for i in range(0,num):
        name=input("Enter the name you want to invite: ")
        print(name,"has been invited")
else:
    print("Too many people!.")

