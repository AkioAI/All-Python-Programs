# 13. Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#
# Sample Pascal's triangle :
#             1
#            1 1
#           1 2 1
#          1 3 3 1
#         1 4 6 4 1
# Pascal's triangle
# Each number is the two numbers above it added together

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)