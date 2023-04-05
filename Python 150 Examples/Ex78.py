shows=["True Detective","Breaking Bad","One Piece","Death Note"]
for index,show in enumerate(shows):
    print(index,show)
another=input("Enter another show: ")
another1=int(int(input("position they want to insert it: ")))
shows.insert(another1,another)
print(shows)
del shows[2]
print(shows)