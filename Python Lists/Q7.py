# 7. Write a Python program to remove duplicates from a list.

def dupl(lst):
    x = set(lst)
    print(list(x))
lst = [1,1,2,3,4,3,2,4,5,6,7,3,2,4,6,3,]
dupl(lst)