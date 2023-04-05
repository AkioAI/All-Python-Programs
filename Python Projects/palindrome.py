print("Enter 'x' for Exit")
num=input("Enter the number to check palindrome:\n")
if  num=='x':
    exit();
else:
    number=int(num)
    orig=number
    rev=0
    while number>0:
          rev=rev*10+number%10
          number//=10
    if orig==rev:
       print(orig,"no. is palindrome")
    else:
       print(orig,"no. is not a palondrome")