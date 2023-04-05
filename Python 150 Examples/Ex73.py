food_dict={}
food1=input("Enter your first favorite food.: ")
food_dict[1]=food1
food2=input("Enter your second favorite food.: ")
food_dict[2]=food2
food3=input("Enter your third favorite food.: ")
food_dict[3]=food3
food4=input("Enter your fourth favorite food.: ")
food_dict[4]=food4
print(food_dict)
dislike=int(input("Which they want to remove? ")
del food_dict[dislike]
print(food_dict)