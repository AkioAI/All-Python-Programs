# 8. Write a Python program to calculate the harmonic sum of n-1. Go to the editor
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# harmonic series

def harmonic_sum(num):
    if num < 2:
        return 1
    else:
        return 1 / num + (harmonic_sum(num-1))
print(harmonic_sum(5))