n = 4
row = 1
while row<=n:
    col = 1
    while col<=n-row+1:
        print(col,end = " ")
        col+=1
    while col<=n:
        print("*",end= " ")
        col+=1
    temp = row-1
    while temp>=1:
        print("*",end = " ")
        temp-=1
    temp = n-row+1
    col = 1
    while col<=n-row+1:
        print(temp,end=" ")
        temp-=1
        col+=1
    print()
    row+=1
