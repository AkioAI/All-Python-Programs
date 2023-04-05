from array import *
arr1=array('i',[])
arr2=array('i',[])
for i in range(0,5):
    num=int(input("Enter a number: "))
    arr1.append(num)
    sorted(arr1)
print(arr1)
for i in arr1:
    print(i)
nums=int(input("Select a number from the above array- "))
if nums in arr1:
    arr1.remove(num)
    arr2.append(nums)
    print(nums)
    print(arr2)
else:
    print("This is not the value of the array")