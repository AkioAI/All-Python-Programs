list={}
for i in range(0,4):
    Name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[Name]={'Age':age,'Shoe Size':shoe_size}
print()
for X in list:
    print((Name),list[Name]['Age'])