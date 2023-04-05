# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end='')
#     print()

n = int(input())
for i in range(0,n):
    for j in range(n,i,-1):
        print(n-i,end=' ')
    print()