# 23. Write a Python program to flatten a shallow list.

# def flat(lst):
#     flat_lst = []
#     for i in lst:
#         for j in i:
#             flat_lst.append(j)
#     return flat_lst
# lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
# print(flat(lst))


# using chain()

import itertools
def flat(lst):
    flat_lst = list(itertools.chain(*lst))
    return flat_lst
lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(flat(lst))