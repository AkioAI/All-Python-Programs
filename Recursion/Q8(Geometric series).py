# 9. Write a Python program to calculate the geometric sum of n-1. Go to the editor
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.

def geom_sum(num):
    if num < 0:
        return 1
    else:
        return 1 / pow(2,num) + geom_sum(num-1)
print(geom_sum(5))