# 6. Write a Python program to get the sum of a non-negative integer.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

def sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum(int(num / 10))
print(sum(1234))