data=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row=int(input("Which row you would like to display: "))
print(data[row])
col=int(input("Which column in that row you would like to display: "))
print(data[row][col])
value=input("Do you want to change the value (y/n): ")
if value=='y':
    num=int(input("Enter value to change: "))
    data[row][col]=num
print(data)



