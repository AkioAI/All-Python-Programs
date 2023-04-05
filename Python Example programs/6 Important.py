# def number():
#     for i in range(1,100):
#         num1=i
#         if num1%5==0:
#             print(num1)

# n=number()

# def display(lst):
#     for i in lst:
#         print(i)
# print("Enter strings seperated by commas: \n")
# lst=[x for x in input().split()]
# display(lst)

###  Lambda Function

# max=lambda x , y: x if x>y else y
# a,b=[int(n) for n in input("Enter two numbers: ").split(',')]
# print("Bigger number:",max(a,b))

###  Lambda using filter() function
###  filter(function,sequence)


# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# lst=[10,23,45,46,70,99]
# lst1=list(filter(is_even,lst))
# print(lst1)


###   lambda using map() function
###  map(function,sequence)


# def squares(x):
#     return x*x
# lst=[1,2,3,4,5,6]
# lst1=list(map(squares,lst))
# print(lst1)


###   Decorators using @decor

# def decor(fun):
#     def inner():
#         value=fun()
#         return value+2
#     return inner
# def decor1(fun):
#     def inner():
#         value=fun()
#         return value*2
#     return inner
# @decor
# @decor1
# def num():
#     return 10
#
# print(num())

#
# def decor(fun):
#     def inner():
#         value=fun()
#         return value+2
#     return inner
# @decor
# def num():
#     return 10
# print(num())

### Decorators

# def decor(fun):
#     def inner():
#         value=fun()
#         return value+2
#     return inner
# def decor1(fun):
#     def inner():
#         value=fun()
#         return value*2
#     return inner
# def num():
#     return(10)
# result_fun=decor(num)
# print(result_fun())


###    Generators

# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g = mygen(5,10)
# for i in g:
#     print(i,end=' ')


# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g = mygen(5,10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


