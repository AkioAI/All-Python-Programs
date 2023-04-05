# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers.

# Type 1
# def gcd(m,n):
#     fm = []
#     for i in range(1,m+1):
#         if (m % i) == 0:
#             fm.append(i)
#     fn = []
#     for j in range(1,n+1):
#         if (n % j) == 0:
#             fn.append(j)
#     cf = []
#     for k in fm:
#         if k in fn:
#             cf.append(k)
#     return (cf[-1])
# print(gcd(12,8))


# Type 2
# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     if m%n == 0:
#         return n
#     else:
#         diff = m-n
#         return(gcd(max(n,diff),min(n,diff)))
# print(gcd(12,8))

# Type 3 (Euclid's Theorem)
# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     while (m%n) != 0:
#         diff = m-n
#         (m,n) = (max(n,diff),min(n,diff))
#
#     return(n)
# print(gcd(12,8))


# Type 4 Euclids Theorem (By Recursion)
def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    if m%n == 0:
        return n
    else:
        return (gcd(n,m % n))     # n > m always
print(gcd(12,8))
print(gcd(54,5))
print(gcd(45,87))
