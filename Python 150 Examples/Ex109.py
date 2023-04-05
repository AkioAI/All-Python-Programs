que=int(input("1) Create a new file\n3) Display the file\n4) Add a new item to the file\nMake a selection 1,2 or 3: "))
if que==1:
    file=open("Subjects.txt",'w')
    file.close()
elif que==2:
    file=open("Subjects.txt",'r')
    for subjects in file:
        print(file)
elif que==3:
    file=open("Subjects.txt",'a')
    str=input("Enter Subject you want to add: ")
    file.write(str)
    file.close()
    file=open("Subjects.txt",'r')
    for subjects in file:
        print(subjects)
else:
    print("Error! , there is no. option that you have typed.")
