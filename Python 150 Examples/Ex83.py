case=True
while case==True:
    str=input("Enter a word in uppercase: ")
    if str.islower():
        print('Try again!')
    else:
        print("right")
        break