from math import*
import math
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
d=(b**2)-(4*a*c)
result1=(-b-math.sqrt(d))/(2*a)
result2=(-b+math.sqrt(d))/(2*a)
print("result is :\n".format(result1,result2))