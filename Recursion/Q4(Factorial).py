# 4. Write a Python program to get the factorial of a non-negative integer.

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num + factorial(num-1)
print(factorial(5))