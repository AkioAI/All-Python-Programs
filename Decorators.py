# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
# def num():
#     return 10
# result_fun = decor(num)
# print(result_fun())

# now the above program is same as the the program shown below

# using @decor
# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
# @decor
# def num():
#     return 10
# print(num())

# program to create two Decorators

# def decor(fun):
#     def inner():
#         value = fun()
#         return value+2
#     return inner
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value/2
#     return inner
# def num():
#     return 10
# result_fun = decor(decor1(num))
# print(result_fun())


# using @ Symbol and create 2 Decorators

# def decor(fun):
#     def inner():
#         value = fun()
#         return value+2
#     return inner
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value*2
#     return inner
# @decor
# @decor1
# def num():
#     return 10
# print(num())

