# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# from functools import *
# def sum(lst):
#     l=reduce(lambda x,y:x+y,lst)
#     return l
# lst= (8, 2, 3, 0, 7)
# print(sum(lst))


# Map With Lambda Function
def sum(lst):
    l=list(map(lambda x:x*x,lst))
    print(l)
lst= (8, 2, 3, 0, 7)
sum(lst)

# Filter with Lambda function
# def sum(lst):
#     l=list(filter(lambda x:x%2==0,lst))
#     print(l)
# lst= (8, 2, 3, 0, 7)
# sum(lst)


# def is_even(x):
#     if x%2==0:
#         return True
#     return False
# lst=[8, 2, 3, 0, 7]
# lst1= list(filter(is_even,lst))
# print(lst1)