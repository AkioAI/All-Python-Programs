num1=int(input("Enter a number: "))
total=num1
again='y'
while again=='y':
    num2=int(input("Enter another number: "))
    total=total+num2
    again=input("Do you want to add another number? (y/n) ")
print("the total is: ",total)


