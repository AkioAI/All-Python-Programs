# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# n = int(input())
# for i in range(1,n+1):
#     for j in range(n+1,i,-1):
#         print(i,end=' ')
#     print()

n = int(input())
for i in range(0,n):
    for j in range(n,i,-1):
        print(i+1,end=' ')
    print()
