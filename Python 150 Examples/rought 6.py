# def print_alpha_nums(abc_list,num_list):
#     for char in abc_list:
#         for num in num_list:
#             print(char,num)
#     return
#
# print_alpha_nums(['a','b','c'],[1,2,3])


def display(lst):
    for i in lst:
        print(i)

print('Enter strings seperated by commas: ')
lst=[x for x in input().split(',')]

display(lst)
