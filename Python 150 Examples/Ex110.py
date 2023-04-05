file=open("Names.txt",'r')
print(file.read())
file.close()
file=open("Names.txt",'r')
selectedname=input("Enter a name from the list: ")
selectedname=selectedname + '\n'
for row in file:
    if row!=selectedname:
        file=open("Names2.txt",'a')
        newrecord=row
        file.write(newrecord)
        file.close()
file.close()
