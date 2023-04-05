# import calendar
# y=int(input("Enter the year: "))
# m=int(input("Enter the month: "))
# print(calendar.month(y,m))



def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())

### Using map function

# def add(x):
#     return x+x
# lst=[8,2,3,0,7]
# lst1=list(map(add,lst))
# print(lst1)

# from functools import *
# def mul(x,y):
#     return x*y
# lst=[2,2,2,2,2]
# lst1=reduce(mul,lst)
# print(lst1)