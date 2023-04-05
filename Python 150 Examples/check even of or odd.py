print("Enter 'x' for Exit")
num=input("enter a number:\n")
if num=='x':
   exit();
try:
   number=float(num)
except ValueError:

else:
check=number%2
if check==0:
print(int(number),"is an even number")
elif check==1:
print(int(number),"is an odd number")
else:
print(number,"number is strange")