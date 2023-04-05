again='y'
count=0
while again=='y':
    name = input("Enter the name you want to invite in the party: ")
    print("%s has been invited to the party" %(name))
    count+=1
    again=input("Do you want to invite somebody else? (y/n) ")
print("%d are coming to your party" %(count))
