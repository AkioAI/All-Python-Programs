# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1
# and itself.

def isprime(num):
    if num<=2:
        pass
    elif num % 2 == 0:
        print(f"{num} is not a prime")
    else:
        print(f"{num} is a prime")
num = int(input("Enter a number: "))
isprime(num)