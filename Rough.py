# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> z=['a','b','c','d','e','f','g','h']
# >>> print(z[::2])
# ['a', 'c', 'e', 'g']
# >>> print(z[:2])
# ['a', 'b']
# >>> print(z[0:2])
# ['a', 'b']
# >>> print(z[0:3])
# ['a', 'b', 'c']
# >>> print(z[::-1])
# ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
# >>> print(z[::-2])
# ['h', 'f', 'd', 'b']
# >>> z.reverse()
# >>> print(z)
# ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
# >>>


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):                        # Child Method
#     print(self.firstname, self.lastname)
#
# #Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()


# import math
# num = int(input("Enter a Number : "))
# rem = ""
# while num >= 1:
#     rem += str(num % 2)
#     num = math.floor(num / 2)
#     binary = ""
# for i in range(len(rem) - 1, -1, -1):
#     binary = binary + rem[i]
# print(f"The Binary format for given number is {binary}")



# for i in range(0,4):
#     print("*"*(i+1))

# for i in range(0,4):
#     print(str(i+1) * (i+1))

# num=int(input("Enter a Number: "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")
#
# def tuples_to_list_str(lst):
#     result = [("%s "*len(el)%el).strip() for el in lst]
#     return result
#
# lst = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# lst = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# print(tuples_to_list_str(lst))
# print(a)


from array import array
import binascii
# array1 = array('i', [7, 8, 9, 10])
# print('array1:', array1)
# as_bytes = array1.tobytes()
# print('Bytes:', binascii.hexlify(as_bytes))


# myNoun = "dog"
# myAdjective = "big"
# myVerb = "ran"
# myAdverb = "quickly"
# print(" The "+ myAdjective +" tall "+ myNoun +" do "+ myVerb+"'s "+ myAdverb +".")

# def __str__(self):
#     selflist = []
#     if self.value == None:
#         return (str(selflist))
#     temp = self.valueself.append(temp.value)
# while temp.next != None:
#     temp = temp.next
#     selflist.append(temp.value)
# return str(selflist)

# class Node:
#     def __init__(self,initial=None):
#         self.value = initial
#         self.next = None
#     def isempty(self):
#         return (self.value == None)
#
#     def append(selfself,v):
#         if self.isempty():
#             self.value = v
#         elif self.next == None:
#             newnode = Node(v)
#             self.next = newnode
#         else:
#             self.next = newnode
#         return()


# l1 = Node(52)
# l2 = Node(534)
# l3 = Node(21)
# l4 = Node(33)
# l5 = Node(2)
# l6 = Node()
# l1.isempty()
# print(Node.isempty(l1))
# print(Node.isempty(l2))
# print(Node.isempty(l3))
# print(Node.isempty(l4))3www22wq
# print(Node.isempty(l5))
# print(Node.isempty(l6))
# print(l1.value)
# print(l2.value)
# print(l3.value)
# print(l4.value)
# print(l5.value)

# def fibonacci(n):
#     fibtable[0] = 0
#     fibtable[1] = 1
#     for i in range(2,n+1):
#         fibtable = fibtable[i-1]+fibtable[i-2]
#     return fibtable[n]
# fibonacci(5)

# def fib(n):
#     if fibtable[n]:
#         return (fibtable[n])
#     if n == 0 or n == 1:
#         value = n
#     else:
#         value = fib(n-1) + fib(n-2)
#     fibtable[n] = value
#     return (value)
# fib(5)

# x = [589,'big',397,'bash']
# y = x[2:]
# u = x
# w = y
# w = w[0:]
# w[0] = 357
# x[2:3] = [487]
# print(x[2])
# print(y[0])
# print(u[2])
# print(w[0])


# first = "kaleidoscope"
# second = ""
# for i in range(len(first)-1,-1,-2):
#   second = first[i]+second
# print(second)
# print(len(first))
#
# a = 10
# id1 = id(a)
# print(id1)
# b = a + 2-2
# id2 = id(b)
# print(id2)

# a = int(input())
# b=int(input())
# C = a+b
# print(C)


# stud1=int(input())
# stud2=int(input())
# stud3=int(input())
# avg = (stud1 + stud2 + stud3) / 3
# print(avg)

# X = int(input())
# N = int(input())
# pow = X ** N
# print(pow)

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# l = x2 - x1
# b = y2 - y1
# area = l*b
# print(area)

# a = int(input())
# b = int(input())
# c = int(input())
# d = (c+a)-b-a
# print(d)

# n = int(input())
# r = n % 2
# is_even = (r == 0)
# if is_even:
#   print(f"{n} is even")
# else:
#   print(f"{n} is odd")

# a = int(input())
# b = int(input())
# c = int(input())
# if b<=a>=c:
#   print(f"{a} is greater.")
# elif a<=a>=c:
#   print(f"{b} is greater.")
# else:
#   print(f"{c} is greater")

# if (10 < 0) and (0 < -10):
#   print("A")
# elif (10 > 0) or False:
#   print("B")
# else:
#   print("C")


# if True or True:
#     if False and True or False:
#         print('A')
#     elif False and False or True and True:
#        print('B')
#     else:
#       print('C')
# else:
#      print('D')

# n = int(input())
# count = 1
# sum = 0
# while count <= n:
#   sum += count
#   count += 1
# print(sum)

# n = int(input())
# count = 1
# sum_even = 0
# while count <= n:
#   if count % 2 == 0:
#     sum_even += count
#   count += 1
# print(sum_even)

# def reverse(n):
# #Implement Your Code Here
#   chn = str(n)
#   if chn == "0":
#     pass
#   else:
#     rev = chn[::-1]
#     return int(rev)
#   return 0
# n=int(input())
# result = reverse(n)
# print(result)

# n = "123"
# rev = n[-1:]
# print(rev)


# i=0
# while i<10:
#   print(i)
# i = i+1

# n = int(input())
# k = 2
# while k <= n:
#   d = 2
#   flag = False
#   while d < k:
#     if (k%d == 0):
#       flag = True
#     d += 1
#   if not(flag):
#     print(k)
#   k += 1



# S = int(input())
# E = int(input())
# W = int(input())
# while S <= E and W <= E:
#   Cel = (S - 32) * (5/9)
#   C = int(Cel)
#   print("{0}\t{1}".format(S,C))
#   S += W




# def checkPalindrome(num):
#   n = str(num)
#   if n == n[::-1]:
#     return True
#   return False
# num = int(input())
# isPalindrome = checkPalindrome(num)
# if (isPalindrome):
#   print('true')
# else:
#   print('false')

# num = str(input())
# even = 0
# odd = 0
# for i in range (0,len(num)):
#   if (int(num[i]) % 2 == 0):
#     even = even + int(num[i])
#   else:
#     odd = odd + int(num[i])
# print(even,"",odd)

# def f(n):
#   if n == 0:
#     return 0
#   elif n == 1 or n == 2:
#     return 1
#   else:
#     return f(n-1)+f(n-2)
# n = int(input())
# print(f(n))


# Calculator
# n= int(input())
# while n!=6:
#     if n==1:
#         a = int(input())
#         b= int(input())
#         x = a+b
#         print(x)
#     elif n ==2:
#         a = int(input())
#         b = int(input())
#         y = a - b
#         print(y)
#     elif n ==3:
#         a = int(input())
#         b = int(input())
#         z = a * b
#         print(z)
#     elif n ==4:
#         a = int(input())
#         b = int(input())
#         p = int(a / b)
#         print(p)
#     elif n ==5:
#         a = int(input())
#         b = int(input())
#         q = a % b
#         print(q)
#     else :
#         print("Invalid Operation")
#     n=int(input())
# ans = []
# count = 0
# while count <= 4:
#   oper = int(input())
#   if oper == 7:
#     a = "Invalid Operation"
#     ans.append(a)
#     break
#   elif oper == 6:
#     break
#   num1 = int(input())
#   num2 = int(input())
#   if oper == 1:
#     add = num1 + num2
#     ans.append(add)
#   elif oper == 2:
#     diff = num1 - num2
#     ans.append(diff)
#   elif oper == 3:
#     prod = num1 * num2
#     ans.append(prod)
#   elif oper == 4:
#     div = num1 // num2
#     ans.append(div)
#   elif oper == 5:
#     mod = num1 % num2
#     ans.append(mod)
#   count += 1
# for i in ans:
#   print(i)



# Pattern 1
#    ****
#    ****
#    ****
#    ****
# n = int(input())
# i = 1
# while i<= n:
#   j = 1
#   while j <=n:
#     print("*",end=' ')
#     j +=1
#   print()
#   i += 1

# Pattern 2
#   4444
#   4444
#   4444
#   4444
# n = int(input())
# i = 1
# while i<= n:
#   j = 1
#   while j <=n:
#     print(n,end='')
#     j +=1
#   print()
#   i += 1


# Pattern 3
# 1234
# 1234
# 1234
# 1234
# n = int(input())
# i = 1
# while i <= n:
#   j = 1
#   while j <= n:
#     print(j,end='')
#     j+=1
#   print()
#   i += 1



#   pattern
# 4321
# 4321
# 4321
# 4321
# n = int(input())
# i = 1
# while i <= n:
#   j = 1
#   while j <= n:
#     print(5-j,end='')
#     j+=1
#   print()
#   i += 1


# Pattern
# 1
# 12
# 123
# 1234
# n = int(input())
# i=1
# while i <= n:
#   j = 1
#   while j <= i:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1



# Pattern
# 1
# 23
# 345
# 4567
# n = int(input())
# i=1
# while i <= n:
#   j = 1
#   p = i
#   while j <= i:
#     print(p,end='')
#     j+=1
#     p+=1
#   print()
#   i+=1




# Pattern
# 1
# 23
# 456
# 789

# n = int(input())
# i=1
# p =1
# while i <= n:
#   j = 1
#   while j <= i:
#     print(p,end='')
#     p+=1
#     j+=1
#   print()
#   i+=1



# Pattern
# *
# **
# ***
# ****
# n = int(input())
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(i+1,end='')
#   print()


# Pattern (Reverse)
# 1
# 21
# 321
# 4321
# n = int(input())
# i=1
# while i <= n:
#   j = 1
#   p = i
#   while j <= i:
#     print(p,end='')
#     j+=1
#     p-=1
#   print()
#   i+=1


# Pattern
# ABCD
# ABCD
# ABCD
# ABCD

# for i in range(1,5):
#   for j in range(65,69):
#     print(chr(j),end='')
#   print()
# OR
# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   while j<=n:
#     # print jth Column
#     charP = chr(ord('A')+j-1)
#     print(charP,end='')
#     j+=1
#   print()
#   i+=1


# Pattern
# ABCD
# BCDE
# CDEF
# DEFG
# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   while j<=n:
#     # print jth Column
#     charP = chr(ord('?')+j+i)
#     print(charP,end='')
#     j+=1
#   print()
#   i+=1
#  OR
# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   start_chr = chr(ord('A')+i-1)
#   while j<=n:
#     # print jth Column
#     charP = chr(ord(start_chr)+j-1)
#     print(charP,end='')
#     j+=1
#   print()
#   i+=1

# Pattern
# A
# BC
# CDE
# DEFG
# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   start_char = chr(ord('A')+i-1)
#   while j<=i:
#     # print jth Column
#     charP = chr(ord(start_char)+j-1)
#     print(charP,end='')
#     j+=1
#   print()
#   i+=1



# Pattern
# E
# DE
# CDE
# BCDE
# ABCDE
# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   start_char = chr(ord('A')+n-i)
#   while j<=i:
#     # print jth Column
#     charP = chr(ord(start_char)+j-1)
#     print(charP,end='')
#     j+=1
#   print()
#   i+=1

# Pattern
# 1
# 11
# 111
# 1111
# n = int(input())
# for i in range(1,n+1):
#   for j in range(1):
#     print(str(1)*i,end='')
#   print()



# num=int(input())
# for i in range(1,num+1):
#     for j in range(0,i):
#         x=i-1
#         if x==0:
#             print(1,end="")
#         else:
#             if x==j or j==0:
#                 print(x,end="")
#             else:print(0,end="")
#     print("")



# pattern
# 1
# 12
# 202
# 3003
# num=int(input())
# for i in range(1,num+1):
#     for j in range(0,i):
#         x=i-1
#         if x==0:
#             print(1,end="")
#         else:
#             if x==j or j==0:
#                 print(x,end="")
#             else:print(0,end="")
#     print("")



# pattern
# 12345
# 1234
# 123
# 12
# 1
# n = int(input())
# for i in range(n+1,1,-1):
#   for j in range(1,i):
#     print(j,end='')
#   print()


# pattern
# A
# BB
# CCC
# EEEE
# FFFFF
# n = int(input())
# i = 1
# while i <= n:
#   j = 1
#   a = chr(ord('A')+i-1)
#   while j <= i:
#     print(chr(ord(a)),end='')
#     j+=1
#   print()
#   i+=1



# pattern
# ****
# ***
# **
# *
# n = int(input())
# for i in range(n+1,1,-1):
#   for j in range(1,i):
#     print("*",end='')
#   print()
# OR
# n = int(input())
# i = 1
# while i <= n:
#   j = 1
#   while j<=n-i+1:
#     print('*',end='')
#     j+=1
#   print()
#   i+=1



# pattern
# 4444
# 333
# 22
# 1
# n = int(input())
# for i in range(n,0,-1):
#   for j in range(1,i+1):
#     print(i,end='')
#   print()




# pattern
#    *
#   **
#  ***
# ****
# n = int(input())
# i = 1
# while i <= n:
#   spaces = 1
#   while spaces <= n-i:
#     print(' ',end='')
#     spaces += 1
#   stars = 1
#   while stars <= i:
#     print(i,end='')
#     stars += 1
#
#   print()
#   i += 1



# Pattern
#    1
#   12
#  123
# 1234
# n = int(input())
# for i in range(1,n+1):
#   for j in range(n,i,-1):
#     print(" ",end='')
#   for z in range (1,i+1):
#     print(z,end='')
#   print()


# Pattern
#    1
#   123
#  12345
# 1234567
# n = int(input())
# for i in range(1,n+1):
#   for j in range(n,i,-1):
#     print(' ',end='')
#   for z in range(i-1,-i,-1):
#     print(i-abs(z),end='')
#   print()
# OR
# n = int(input())
# i = 1
# while i <= n:
#   spaces = 1
#   # spaces
#   while spaces <= n-i:
#     print(' ',end='')
#     spaces+=1
#   p = 1
#   j = 1
#   # increasing seq
#   while j <= i:
#     print(p,end='')
#     j+=1
#     p+=1
#     # decreasing seq
#   p = i-1
#   while p>=1:
#     print(p,end='')
#     p-=1
#   print()
#   i+=1


# n = int(input())
# for i in range(1,n+1):
#   for j in range(n,i,-1):
#     print(' ',end='')
#   for z in range(i-1,-i,-1):
#     print("*",end='')
#   print()


# n = int(input())
# for i in range(1,n+1):
#   for j in range(n,i,-1):
#     print(' ',end='')
#   for z in range(i-2,-i,-1):
#     print(i-abs(z),end='')
#   print()



# n = int(input())
# i = 1
# while i <= n:
#   spaces = 1
#   # spaces
#   while spaces <= n-i:
#     print(' ',end='')
#     spaces+=1
#   p = 0
#   j = 1
#   # increasing seq
#   while j <= i:
#     print(p+i,end='')
#     j+=1
#     p+=1
#   # decreasing seq
  # p = 0
  # j = 1
  # while j>=i:
  #   print(p-i,end='')
  #   j+=1
  #   p+=1
  # print()
  # i+=1


# n = int(input())
# for i in range(n,-(n),-1):
#     for j in range(1,abs(i)+1):
#         print(' ',end='')
#     for z in range(n,abs(i),-1):
#         print('* ',end='')
#     print()




# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     space=1
#     while space<=(n-i)*2:
#         print(" ",end="")
#         space+=1
#     reverse=i
#     while reverse>=1:
#         print(reverse,end="")
#         reverse-=1
#     print()
#     i+=1


# n = int(input())
# i = 1
# while i <= n:
#   space = 1
#   while space <= n - i:
#     print(" ", end="")
#     space = space + 1
#   j = 1
#   p = i
#   while j <= i:
#     print(p, end='')
#     p -= 1
#     j = j + 1
#   p = 1
#   x = 2 * i -
#   while p <= i - 1:
#     print(x, end='')
#     p = p + 1
#     x = x + 1
#
#   print()
#   i = i + 1



# Pattern
# 1111
# 000
# 11
# 0
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i,-1,-1):
#         if (i%2==0):
#             print("0",end='')
#         else:
#             print("1",end='')
#     print()



#     *
#    ***
#   *****
#    ***
#     *
# n = int(input())
# for i in range(n):
#   if i< n//2:
#     for j in range(n//2-i):
#       print(" ",end='')
#     for k in range(2*i+1):
#       print("*",end='')
#     print()
#   elif i==n//2:
#     for i in range(n):
#       print("*",end='')
#     print()
#   else:
#     for j in range(i-n//2):
#       print(" ",end='')
#     for k in range((n-i)*2-1):
#       print("*",end='')
#     print()




# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
# n = int(input())
# k=(n*2)-1
# low=0
# high=k-1
# value= n
# matrix = [[0 for i in range(k)] for j in range(k)]
# for i in range(n):
#   for j in range(low,high+1):
#     matrix [i][j] = value
#   for j in range(low+1,high+1):
#     matrix [j][i] = value
#   for j in range(low+1,high+1):
#     matrix [high][j] = value
#   for j in range(low+1,high):
#     matrix [j][high] = value
#   low+=1
#   high-=1
#   value-=1
#
# for i in range(k):
#   for j in range(k):
#     print(matrix[i][j],end='')
#   print()




#      1
#     212
#    32123
#   4321234
# n =int(input())
# for i in range(1,n+1):
#   for j in range(1,n-i+1):
#     print(" ",end='')
#   for j in range(i,0,-1):
#     print(j,end='')
  # for j in range(2,i+1):
  #   print(j,end='')
  # print()


# def printTable(start, end, step):
#   for i in range(start,end+1,step):
#     C = int((i-32)*(5/9))
#     print("{0}\t{1}".format(i,C))
# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s, e, step)



# def checkMember(n):
# #Implement Your Code Here
#   if n==0:
#     return 0
#   elif n == 1 or n == 2:
#       return 1
#   else:
#     f = (checkMember(n-1)+checkMember(n-2))
#   print(f)
# n=int(input())
# if(checkMember(n)):
#     print("true")
# else:
#     print("false")



# n = 100
# a = 0
# b = 1
# sum = 0
# f = []
# count = 1
# # print("Fibonacci Series: ", end = " ")
# while(count <= n):
#   print(f, end = " ")
#   a = b
#   b = sum
#   sum = a + b
#   f.append(sum)
#   count += 1
# a = int(input())
# if a in f:
#     print("True")
# else:
#     print("False")



# def checkMember(n):
# #Implement Your Code Here
#     num = 100
#     a = 0
#     b = 1
#     sum = 0
#     f = []
#     count = 1
# # print("Fibonacci Series: ", end = " ")
#     while (count <= num):
#         # print(f, end=" ")
#         a = b
#         b = sum
#         sum = a + b
#         f.append(sum)
#         count += 1
#     if n in f:
#         return True
#     else:
#         return False
# n=int(input())
# if(checkMember(n)):
#     print("true")
# else:
#     print("false")


# def checkPalindrome(num):
#     num = str(num)
#     if num == num[::-1]:
#         return True
#     else:
#         return False
#
#
# num = int(input())
# isPalindrome = checkPalindrome(num)
# if (isPalindrome):
#     print('true')
# else:
#     print('false')



#
# def armstrong(num):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     if num == sum:
#         return "true"
#     else:
#         return "false"
# num = int(input())
# # display the result
# print(armstrong(num))






# #main
# t = int(stdin.readline().rstrip())
#
# while t > 0 :
#     arr, n = takeInput()
#     if n != 0 :
#         swapAlternate(arr, n)
#         printList(arr, n)
#     t -= 1

# for i in range(6,0,-1):
#     for j in range(i,6):
#         print(" ",end='')
#     p = 1
#     for k in range(1,i+1):
#         print(p,end='')
#         p+=1
#     print()
#     for j in range(i,6):
#         print(" ",end='')
#     p = 1
#     for k in range(1,i+1):
#         print(p,end='')
#         p+=1
#     print()




# sum = 0
# k = int(input())
# a = [x for x in input().split()]
# # print(a)
# for j in a:
#     b = int(j)
#     sum+=b
# print(sum)



import numpy as np
# r = 2 * np.random.randint(0, 2, size=(5,5))
# print(r)




# a = [x for x in input().split()]
# b = set(a)
# for i not in b:
#     print(i)

#
# a = [1,2,3,2,1]
# for i in range (0,n):
#     for j in range(i+1,n):
#         if arr
# print(b)



# from functools import *
# lst = [int(x) for x in input().split()]
# result = reduce(lambda x,y:x+y,lst)
# print(result)

# n=int(input())
# low = 1
# high = n+1
# for i in range(n,0,-1):
#     for j in range(i,n):
#         # if j == n-i:
#         print("*",end='')
#     for j in range(low,i+1):
#         print(j, end = '')
#         low+=1
#         # j+=1
#     print()



# Swap Alternate
# def rev(li):
#     l = len(li)
#     if l%2 == 0:
#         for i in range(0,l,2):
#             li[i],li[i+1] = li[i+1],li[i]
#     else:
#         for i in range(0,l-1,2):
#             li[i],li[i+1] = li[i+1],li[i]
#     for i in li:
#         print(i,end =' ')
# n = int(input())
# li = [int(x) for x in input().split()[:n]]
# rev(li)


# Unique value in the list
# li = [1,2,3,4,1,2,3]
# a = set([x for x in li if li.count(x) == 1])
# print(list(a))
# a = set(li)
# for i in a:
#     if li.count(i) == 1:
#         print(i)

# counting value which occur 1 time only
# li = [1,2,3,4,1,2,3]
# # a = set([x for x in li if li.count(x) == 1])
# a = set(li)
# for i in a:
#     if li.count(i) == 1:
#         print(i)

# arr = [1,2,3,4,5,6,7 ]
# x =12
# count = 0
# for i in range(0, len(arr)):
#     for j in range(i + 1, len(arr)):
#         for k in range(j + 1, len(arr)):
#             if arr[i] + arr[j] + arr[k] == x:
#                 count += 1
# print(count)




# arr = [0,1,1,0,1,0,1]
# arr.sort()
# print(arr)




# ans = 0
# n = [x for x in input().split()]
# print(n)
# for i in range(len(n)):
#     a=int(n[i])
#     c = a**len(n)
#     ans+=c
# print(ans)
# # if ans == n or ans == 1 or ans==0:
# #     print("true")
# # else:
# #     print("false")

# Armstrong
# def armstrong(num):
#     sum = 0
#     temp = num
#     a = str(num)
#     b = len(a)
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** b
#         temp //= 10
#     if num == sum:
#         return True
#     else:
#         return False
# num = int(input())
# isarmstrong = armstrong(num)
# # display the result
# if (isarmstrong):
#     print('true')
# else:
#     print('false')
#
# arr1 = [2,6,1,2]
# arr2 = [1,2,3,4,2]
# for value in arr1:
#     if value in arr2:
#         print(value)




# class Solution(object):
#    def intersect(self, nums1, nums2):
#       """
#       :type nums1: List[int]
#       :type nums2: List[int]
#       :rtype: List[int]
#       """
#       m = {}
#       if len(nums1)<len(nums2):
#          nums1,nums2 = nums2,nums1
#       for i in nums1:
#          if i not in m:
#             m[i] = 1
#          else:
#             m[i]+=1
#       result = []
#       for i in nums2:
#          if i in m and m[i]:
#             m[i]-=1
#             result.append(i)
#       return result
# ob1 = Solution()
# print(ob1.intersect([2,6,1,2], [1,2,3,4,2]))


# def bubble_sort(arr):
#    for i in range(len(arr)-1):
#       for j in range(len(arr)-1):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#    return arr
# arr = [2,13,4,1,3,6,28]
# a = bubble_sort(arr)
# print(a)


# def bubble_sort(arr1,arr2,output):
#    for i in range(len(arr1)-1):
#       for j in range(1,len(arr2)-1):
#          output = arr1[i] + arr[j]
#
#    return arr
# arr1 = [1,3,4,7,11]
# arr2 = [2,4,6,13]
# arr = arr1 + arr2
# a = bubble_sort(arr)
# print(a)



# Pattern  (n = 6)
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456
# n = int(input())
# p = n-1
# for i in range(1,n+1):
#    for j in range(i-1):
#       print(" ",end='')
#    for j in range(i,n+1):
#       print(j,end='')
#    print()
# for i in range(n-1,0,-1):
#    for j in range(1,i):
#       print(" ",end='')
#    for j in range(i,n+1):
#       print(j,end='')
#    print()

# Pattern
# 1 2 3 4 5
# 11 12 13 14 15
# 21 22 23 24 25
# 16 17 18 19 20
# 6 7 8 9 10
# import math
# n = int(input())
# for i in range(math.ceil(n/2)):
#    for j in range(1,n+1):
#        print(n*2*i + j,end = " ");
#    print()
# for i in range(n//2,0,-1):
#    for j in range(1,n+1):
#        print(n*(2*i-1) + j , end = " ")
#    print()


# def rotate(arr,d,n):
#     for i in range(d):
#         rotation(arr,n)
#
# def rotation(arr,n):
#     temp = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp
#
# def printarray(arr,n):
#     for i in range(n):
#         print("% d" % arr[i], end=" ")
#
# arr = [1,2,3,4]
# rotate(arr, 2, 4)
# printarray(arr, 4)


# arr = [90,8,90,5]
# lst = []
# a = max(arr)
# arr.remove(a)
# print(max(arr))
# a = [x for x in arr if all arr.count(x) >= 2]
# print(a)
# else:
#     for i in arr:
#         a = max(arr)
#     lst.append(a)
#     arr.remove(a)
#     for i in arr:
#         b = max(arr)
#     lst.append(b)
#     print(arr)
#     print(lst)


# arr1 = [8,5,2]
# arr2 = [1,3]
# a = [len(arr1), len(arr2)]
# b = max(a)
# print(b)
# output = [arr1[i] + arr2[i] for i in range(b)]
# print(output)


#
# arr = []
# a = [x for x in arr if arr.count(x) == len(arr)]:
#
#     print("-2147483648")
# else:
#     a = set(arr)
#     b = list(a)
#     b.sort()
#     print(b[-2])



# def bubble_sort(A):
#     for i in range(len(A)):
#         for k in range(len(A)-1,i,-1):
#             if (A[k]<A[k-1]):
#                 swap(A,k,k-1)
# def swap(A,x,y):
#     A[x],A[y] = A[y],A[x]
# A = [534,246,933,127,277,321,454,565,220]
# bubble_sort(A)
# print(A)


# arr1 = [1,3,4,7,11]
# arr2 = [2 ,4 ,6 ,13]
# arr = arr1 + arr2
# for i in range(len(arr)):
#     for j in range(len(arr) - 1, i, -1):
#         if arr[j] < arr[j - 1]:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#         else:
#             print("-2147483648")
# print(arr[-2])


# def per(a,b):
#     for i in range(len(a)):
#         if a[i] in b[i]:
#             return True
#         else:
#             return False
# a = "race"
# b = "rate"
# print(per(a,b))

# arr = []
# arr2 = []
# a = "Welcome to Coding Ninjas"
# b = [x for x in a.split()]
# for i in b:
#     arr.append(i[::-1])
# for i in arr:
#     arr2.append(i)
# print(arr2)




# str = "aabccbaa"
# b = []
# x = 'a'
# for i in str:
#     b.append(i)
# print(b)
# a = [x for x in b if b.count(x)>2]
# c = len(a)
# print(a)
# temp = 1
# while temp <= c:
#     for i in b:
#         if x in b:
#             b.remove(x)
#     temp+=1
# for i in b:
#     print(i,end='')


# str  = "abdefgbabfba"
# str1 = []
# for i in str:
#     str1.append(i)
# print(str1)
# for i in range(len(str1)):
#     if str1[i] == str1[i]



# Remove Character
# a = "aabccbaa"
# b = []
# for i in a:
#     b.append(i)
# for i in range(0,len(b)-1):
#     for j in range(len(b)-1):
#         if b[j] == b[j+1]:
#            b.remove(b[j])
# print(b)


#  Check Permutation
# from math import *
# str1= "abc"
# str2 = "cbd"
# str3 = str1+str2
# b = len(str3)
# count = 0
# if len(str1) == len(str2):
#     for i in range(0,len(str1)):
#         temp = i
#         for j in range(0,len(str2)):
#             if str1[temp] == str2[j]:
#                 count+=1
#     print(count)
#     print(floor(b/2))
#     if b // 2 == count:
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")




