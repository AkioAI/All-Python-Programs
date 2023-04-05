from math import*
print("1) Square")
print("2) Trangle")
print()
menuselection=int(input("choose a number: "))
if menuselection==1:
    length=float(input("Enter the length: "))
    Area=length*2
    print(Area)
elif menuselection==2:
    base=float(input("Enter the base: "))
    height=float(input("input Enter the height: "))
    Area=(1/2)*base*height
    print(Area)
else:
    print("Sorry! choose 1 or 2 only.")
