# 4. Write a Python program to get the smallest number from a list.

def small_num(lst):
    for i in lst:
        a = min(lst)
    print(a)
lst = [3,66,552,-233,2,23,526,0,-47,574,67,-456,-36,-34,2,5]
small_num(lst)