# 1. Write a Python function to find the Max of three numbers.

# def maxno(a,b,c):
#     maxnum=max(a,b,c)
#     print(maxnum)
# maxno(2,3,5)

# OR

def max_two_nums(a,b):
    if a>b:
        return a
    return b
def max_three_nums(a,b,c):
    return max_two_nums(a,max_two_nums(b,c))     #Recursion
a=int(input("Enter first number: ",))
b=int(input("Enter second number: ",))
c=int(input("Enter third number: ",))
print(max_three_nums(a,b,c))