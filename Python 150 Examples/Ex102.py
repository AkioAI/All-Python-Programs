list={}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name]={'Age':age,'Shoe Size':shoe_size}
print()
ask=input("Enter a name: ")
print(list[ask])