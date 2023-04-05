from array import *
nums=array('i',[])
while len(nums)<5:
    num=int(input("Enter a number between 10 and 20: "))
    if 10<num<20:
        nums.append(num)
    else:
        print("Outside the range")
print("Thank you!")
for i in nums:
    print(i)
