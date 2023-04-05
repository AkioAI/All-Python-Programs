# 2. Write a Python program to multiplies all the items in a list.

from functools import *
def mul(lst):
    a = reduce(lambda x,y:x*y,lst)
    print(a)

lst = [1,2,3,4,5]
mul(lst)