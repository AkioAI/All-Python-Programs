que=input("which direction you want to count (up or down)?")
if que=='up':
    num=int(input("Choose the top number"))
    for i in range(1,num):
        print(i)
if que=='down':
    num1=int(input("Choose a number below 20"))
    for x in range(20,num1-1,-1):
        print(x)
else:
    print("don’t understand")

