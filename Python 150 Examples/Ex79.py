num=[]
count=0
while count<3:
    num1=int(input("Enter the number. "))
    num.append(num1)
    print(num)
    count+=1
lastnum=input("Do you want to enter last no.: (y/n)")
if lastnum=='n':
    num.remove(num1)
print(num)