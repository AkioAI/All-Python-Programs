num=10
while num>0:
    print("There are %d green bottles hanging on the wall,\n"
          "%d green botles hanging on the wall,\n"
          "and if 1 green bottle should accidentally fall.\n" %(num,num))
    num-=1
    ans=int(input("how many green bottles will be hanging on the wall? "))
    if ans==num:
        print("There will be",num," green bottles hanging on the wall")
    else:
        while ans!=num:
            print("No, try again!")
            break
print("There are no more green bottles hanging on the wall")