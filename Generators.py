def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g = mygen(5,10)
for i in g:
    print(i,end=' ')

# WAP to create a Generators

# def mygen(x,y):
#     while x<=y:
#         yield x
#         x += 1
# g = mygen(5,10)
#
# for index,i in enumerate(g,start=1):
#     print(index,"\t",i)


# A Generator that returns characters from A to C

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g = mygen()
# print(next(g))
# print(next(g))
# print(next(g))

