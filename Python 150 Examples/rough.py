i=0
while i<10:
    print("i is now {}".format(i))
    i+=1


print("------------\n")


for x in range(20):
    print("x is now {}".format(x))


print("-----------")


#available_exit=["east","West","North","South"]
#chosen_exit='East','West','South'
#while chosen_exit not in available_exit:
 #   chosen_exit=input("Please choose a direction: ")
#print("you should be glad you got out from there.")


print("------------")


#available_exit=["east","West","North","South"]
#chosen_exit=''
#while chosen_exit not in available_exit:
 #   chosen_exit=input("Please choose a direction: ")
  #  if chosen_exit.casefold() == "quit":
  #      print("Goodbye!..")
   #     break
    #print("you should be glad you got out from there.")



print("-------------")



for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        break