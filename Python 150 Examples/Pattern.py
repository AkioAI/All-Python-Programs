# for i in range(0, 9):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print("*",end="")
#     print()


#     *
#    **
#   ***
#  ****
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j>=5-i:
#             print("*",end="")
#         else:
#             print(" ",end='')
#     print()


# ****
# ***
# **
# *
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=(n+1)-i:
#             print("*",end="")
#     print()


#       *
#     * * *
#   * * * * *
# * * * * * * *
# for i in range(1,5):
#     for j in range(1,9):
#         if j>=5-i and j<=3+i:
#             print("*",end='')
#         else:
#             print(' ',end="")
#     print()

# * * * * * * *
#   * * * * *
#     * * *
#       *
# for i in range(1,5):
#     for j in range(1,8):
#         if j>=i and j<=8-i:
#             print("*",end='')
#         else:
#             print(' ',end='')
#     print()



# *******
# *** ***
# **   **
# *     *
# for i in range(1,5):
#     for j in range(1,8):
#         if j<=5-i or j>=3+i:
#             print("*",end="")
#         else:
#             print(" ",end='')
#     print()


# 1
# 12
# 123
# 1234
# for i in range(1,5):
#     for j in range(1,5):
#         if j<=i:
#             print(j,end='')
#         else:                              # not compulsory
#             print(" ",end='')
#     print()


# for i in range(0,7):
#     for j in range(0,5):
#         if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
#             print("*",end='')
#         else:
#             print(" ",end="")
#     print()

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (i == 2*i):
#             if j<=n-i:
#                 print('1',end='')
#         elif j<=n-i:
#             print('0',end='')
#     print()


# for i in r4
# ange(1,6):
#     for j in range(1,6):
#             if (j<2+i and j<=5) and (j>4-i and j<=1):
#                 print("*",end="")
#             else:
#                 print(" ",end='')
#     print()

n = int(input())
for i in range(1,n+1):
    for j in range(n-i,-1,-1):
        if (i%2==0):
            print("0",end='')
        else:
            print("1",end='')
    print()