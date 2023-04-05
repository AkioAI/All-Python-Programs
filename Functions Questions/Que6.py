# 6. Write a Python function to check whether a number is in a given range.

def find(l,x):
    for i in range(len(l)):
        if l[i]==x:
            print(i)
l=[1,2,3,32,56]
x=3
find(l,x)