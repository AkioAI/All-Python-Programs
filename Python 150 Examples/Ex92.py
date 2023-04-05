from array import *
import random
arr1=array('i',[])
arr2=array('i',[])
arr3=array('i',[])
while len(arr1)<3:
    nums=int(input("Enter number: "))
    arr1.append(nums)
    print(arr1)
for i in range(0,5):
    nums1=random.randint(0,3)
    arr2.append(nums1)
    print(arr2)
arr3=arr1+arr2
print(arr3)
newarr=sorted(arr3)
print(newarr)
for i in newarr:
    print(i)

