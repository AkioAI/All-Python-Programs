# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print(n,end=' ')
#     print()

n = int(input())
for i in range(0,n):
    for j in range(n,i,-1):
        print(n,end=' ')
    print()