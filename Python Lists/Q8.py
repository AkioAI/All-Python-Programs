# 8. Write a Python program to check a list is empty or not.

def check(lst):
    if len(lst) == 0:
        return True
    return False
print(check(lst=[]))
print(check(lst=[2]))
print(check(lst=[1,2]))