name=input("Enter your name: ")
num=int(input("Enter a number: "))
if num<10:
    dis=name*num
    print(dis)
else:
    for i in range(0,3):
        print("too high")