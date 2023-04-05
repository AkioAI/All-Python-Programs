total=0
for i in range(0,5):
    num=int(input("Enter a number: "))
    ask=input("Do you want to add this number? y/n")
    if ask=='y':
        num=num+total
        print(num)
print(total)