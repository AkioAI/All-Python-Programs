def add_name():
    str=input("Enter a name you want to add to the list: ")
    names.append(str)
    return names
def change_name():
    for index,x in enumerate(names, start=0):
        select_num=int(input("Enter the no. of the name you want to change: "))
        new_name=input("Enter a name: ")
        names[select_num]=new_name
        return names
def delete_name():
    for index,x in enumerate(names, start=0):
        select_num = int(input("Enter the no. of the name you want to delete: "))
        del names[select_num]
        return names
def view_name():
    for x in names:
        print(x)
    print()
def menu():
    temp = 'y'
    while temp == 'y':
        select = int(input("make your selection:\n1) Add names.\n2)Change names.\n3)delete names.\n4)view names.\n"
                           "5) Quit\n\n"))
        if select == 1:
            names = add_name()
        elif select == 2:
            names = change_name()
        elif select == 3:
            names = delete_name()
        elif select == 4:
            names = view_name()
        elif select == 5:
            temp = 'n'
        else:
            print("Error!, I cannot find the number you choose ")
        data = (names,temp)
names = []
menu()

