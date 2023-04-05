# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique(lst):
    s=set(lst)
    new_lst=list(s)
    print(f"Sample list: {lst}")
    print(f"Unique list: {new_lst}")
lst = [1,2,3,3,3,3,4,5]
unique(lst)