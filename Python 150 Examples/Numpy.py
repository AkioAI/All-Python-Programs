from array import*
x=int(input("Enter the length of array:"))
arr=array('i',[ ])
for i in range(x):
    y=int(input("enter the next value:"))
    arr.append(y)
print("array is",end=":-")
print(arr)
z=int(input("Enter a number to search and destroy"))
k=0
for p in range (len(arr)):
   for c in arr:
       if c==z:
          arr.remove(c)
          print("index value is:-%d"%(k),end=",")

          print()
          print("deleted element from array is:-%d"%(c))
          print(arr)
