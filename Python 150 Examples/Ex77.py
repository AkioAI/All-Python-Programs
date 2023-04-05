name1=input("Enter the first names you want to invite: ")
name2=input("Enter the second names you want to invite: ")
name3=input("Enter the third names you want to invite: ")
names=[name1,name2,name3]
print(names)
str =input("Do you want to add another name: (y/n)")
while str=='y':
    name4=names.append(input("Enter another name: "))
    str = input("Do you want to add another name: (y/n)")
print('you have invited',len(names),'people in your party.')
print(names)
str1=input("Enter one of the names from the above: ")
ind=names.index(str1)
print(ind)
cut=input("Do you still want to this person to come in party? (y/n)")
if cut=='n':
    del names[ind]
    print(names)