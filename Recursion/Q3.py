# 3. Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def recr_lst(lst):
    total = 0
    for element in lst:
        if type(element) == type([]):
            total = total + recr_lst(element)
        else:
            total = total+element
    return total
print(recr_lst([1, 2, [3,4], [5,6]]))