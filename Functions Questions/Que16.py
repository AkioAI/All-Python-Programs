#6. Write a Python function to create and print a list where the values are square of numbers between
# 1 and 30 (both included).

def square(lst):
    l=list(map(lambda x:x*x,lst))
    print(l)
lst=[]
for i in range(1,31):
    lst.append(i)
square(lst)