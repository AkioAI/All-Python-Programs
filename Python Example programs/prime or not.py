temp=0
while temp==0:
    num=int(input("Enter a number: "))
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime.")
            break
        else:
            print(num,"is a prime")
