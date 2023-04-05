data=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row=int(input("Which row you would like to display: "))
print(data[row])
new_value=int(input("Enter a new value: "))
data[row].append(new_value)
print(data)