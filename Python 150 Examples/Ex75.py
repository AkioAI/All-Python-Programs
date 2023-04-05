num=[123,245,568,452,256]
for index,nums in enumerate(num):
    print(index,':',nums)
str=int(input("Enter a three digit number: "))
if str in num:
    print(num.index(str))
else:
    print("That is not[ in the list")