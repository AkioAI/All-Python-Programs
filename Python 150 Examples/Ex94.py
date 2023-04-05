from array import *
arr1=array('i',[])
while True:
    for i in range(0,5):
        num=int(input("Enter a number: "))
        arr1.append(num)
        sorted(arr1)
    print(arr1)
    nums=int(input("Select a number from the above array- "))
    if nums in arr1:
        print("the position of",nums,"is",arr1.index(nums))
    else:
        print("Try again")
