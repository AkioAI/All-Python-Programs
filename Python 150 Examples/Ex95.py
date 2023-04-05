from array import *
import random
arr1=array('i',[])
for i in range(0,5):
    num=random.randint(10,100)
    arr1.append(num)
    print(arr1)
num1=int(input("Enter whole number between 2 and 5: "))
if 2<num1<5:
    for i in range(0,5):
        res=arr1[i]/num1
        print(round(res,2))
else:
    print("try again")