# 1. Write a Python program to calculate the sum of a list of numbers.

def sum(num_lst):
    if len(num_lst) == 1:
        return num_lst[0]
    else:
        return num_lst[0]+sum(num_lst[1:])
num_lst = [1,3,4,2,5,6,3,4,2,67,89,65,24]
print(sum(num_lst))