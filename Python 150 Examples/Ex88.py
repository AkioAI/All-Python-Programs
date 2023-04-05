from array import *
num=array('i',[])
for i in range(0,5):
    nums=int(input("Enter a number: "))
    num.append(nums)
num=sorted(num)
num.reverse()
print(num)