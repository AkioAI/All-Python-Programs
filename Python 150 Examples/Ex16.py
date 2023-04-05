raining=input("Is it raining? ")
raining=str.casefold(raining)
if raining=='yes':
    str.casefold(raining)
    windy=input("Is it windy? ")
    if windy=='yes':
        str.casefold(windy)
        print("It is too windy for an Umbrella")
    else:
        str.casefold(windy)
        print("Take an Umbrella")
else:
    print("Have a nice day")

