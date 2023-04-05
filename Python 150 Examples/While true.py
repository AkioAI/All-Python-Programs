while True:
    print("Enter 'x' for exit")
    name=input("Enter your name:")
    ntime=int(input("How many time you wanted to write your name?"))
    if  name=='x':
        break
    else:
        for i in range(0,ntime):
           print(name)
print()
