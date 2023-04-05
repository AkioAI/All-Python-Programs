# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the
# number as an argument.

# Factorial
def factorial(num):
    if (num == 1) or (num == 0):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(4))