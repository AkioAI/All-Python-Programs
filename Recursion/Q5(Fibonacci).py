# 5. Write a Python program to solve the Fibonacci sequence using recursion.

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))
    # return

a = int(input())
print(fibonacci(a))
for i in range(a):
    print(fibonacci(i),end=' ')
