# 27. Write a Python program to find the second smallest number in a list.

lst = [10, 20, 30, 40, 50, 60, 1, 34, 23, 3, 5, -2, 34]
first_small = min(lst)
remv = lst.remove(first_small)
second_small = min(lst)
print(f"first smallest number in the list is: {first_small}")
print(f"second smallest number in the list is: {second_small}")
