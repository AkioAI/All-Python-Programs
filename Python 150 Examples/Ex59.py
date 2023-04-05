import random as rd
colours=rd.choice(['red','blue','green','brown','yellow'])
print("Select from: red,blue,green,brown,yellow")
print()
temp=True
while temp==True:
    choose = input("Pick any colour: ")
    choose=choose.lower()
    if colours==choose:
        print("Well Done!")
    else:
        if colours=='Red':
            print("I bet you are seeing red right right now.")
        elif colours=='Blue':
            print("Don't feel Blue.")
        elif colours=='Green':
            print("I bet you are green with envy right now.")
        elif colours=='Brown':
            print("I know your door is brown.")
        elif colours=='Yellow':
            print("Mike got the yellow teeths")
