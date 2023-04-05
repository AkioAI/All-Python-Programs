# 25. Write a Python program to select an item randomly from a list.
import random as r
def rndm(lst):
    item = r.choice(lst)
    print(item)
lst = ['Python', 1, '43', 34, 213, 'Sketching', 'Javascript', 'Sakura', 'kisho']
rndm(lst)