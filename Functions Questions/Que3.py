# 3. Write a Python function to multiply all the numbers in a list.

# from functools import reduce
# def multiply(lst):
#     mul= reduce(lambda x,y:x*y,lst)
#     return mul
# lst=[8, 2, 3, -1, 7]
# print(multiply(lst))

def multiply(l):
    total=1
    for i in l:
        total *= i
    return total
l= (8, 2, 3, -1, 7)
print(multiply(l))