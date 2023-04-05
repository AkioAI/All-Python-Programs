list={}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name]={'Age':age,'Shoe Size':shoe_size}
print()
for name in list:
    print((name),list[name]['Age'])
remove=input("Enter the name to remove: ")
del list[remove]
print(list)