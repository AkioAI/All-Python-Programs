file=open("names.txt",'a')
new_name=input("Enter the name to add: ")
file.write(new_name +"\n")
file.close()
