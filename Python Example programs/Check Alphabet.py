temp=0
while temp==0:
    alpha=(input("Enter any Character: "))
    if ((alpha>='a' and alpha<='z') or (alpha>='A' and alpha<='Z')):
        print(alpha,"is an alphabet")
    else:
        print("%s is not an alphabet"%(alpha))