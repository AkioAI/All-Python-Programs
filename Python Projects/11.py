def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))


# Factorial by using Lambda function
factorial=lambda n:1 if n==0 else n*factorial(n-1)
print(factorial(4))