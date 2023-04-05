Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import*
>>> for i in range(1,20)
SyntaxError: invalid syntax
>>> for i in range(1,20):
	print("No. {0} square is {1} and cube is {2}".format(i,i**2,i**3))

	
No. 1 square is 1 and cube is 1
No. 2 square is 4 and cube is 8
No. 3 square is 9 and cube is 27
No. 4 square is 16 and cube is 64
No. 5 square is 25 and cube is 125
No. 6 square is 36 and cube is 216
No. 7 square is 49 and cube is 343
No. 8 square is 64 and cube is 512
No. 9 square is 81 and cube is 729
No. 10 square is 100 and cube is 1000
No. 11 square is 121 and cube is 1331
No. 12 square is 144 and cube is 1728
No. 13 square is 169 and cube is 2197
No. 14 square is 196 and cube is 2744
No. 15 square is 225 and cube is 3375
No. 16 square is 256 and cube is 4096
No. 17 square is 289 and cube is 4913
No. 18 square is 324 and cube is 5832
No. 19 square is 361 and cube is 6859
>>> for i in range(1,20):
	print("No. {0:2} square is {1:4} and cube is {2:4}".format(i,i**2,i**3))

	
No.  1 square is    1 and cube is    1
No.  2 square is    4 and cube is    8
No.  3 square is    9 and cube is   27
No.  4 square is   16 and cube is   64
No.  5 square is   25 and cube is  125
No.  6 square is   36 and cube is  216
No.  7 square is   49 and cube is  343
No.  8 square is   64 and cube is  512
No.  9 square is   81 and cube is  729
No. 10 square is  100 and cube is 1000
No. 11 square is  121 and cube is 1331
No. 12 square is  144 and cube is 1728
No. 13 square is  169 and cube is 2197
No. 14 square is  196 and cube is 2744
No. 15 square is  225 and cube is 3375
No. 16 square is  256 and cube is 4096
No. 17 square is  289 and cube is 4913
No. 18 square is  324 and cube is 5832
No. 19 square is  361 and cube is 6859
>>> for i in range(1,20):
	print("No. {0:2} square is {1:<4} and cube is {2:<4}".format(i,i**2,i**3))

	
No.  1 square is 1    and cube is 1   
No.  2 square is 4    and cube is 8   
No.  3 square is 9    and cube is 27  
No.  4 square is 16   and cube is 64  
No.  5 square is 25   and cube is 125 
No.  6 square is 36   and cube is 216 
No.  7 square is 49   and cube is 343 
No.  8 square is 64   and cube is 512 
No.  9 square is 81   and cube is 729 
No. 10 square is 100  and cube is 1000
No. 11 square is 121  and cube is 1331
No. 12 square is 144  and cube is 1728
No. 13 square is 169  and cube is 2197
No. 14 square is 196  and cube is 2744
No. 15 square is 225  and cube is 3375
No. 16 square is 256  and cube is 4096
No. 17 square is 289  and cube is 4913
No. 18 square is 324  and cube is 5832
No. 19 square is 361  and cube is 6859
>>> for i in range(1,20):
	print("No. {0:2} square is {1:>4} and cube is {2:>4}".format(i,i**2,i**3))

	
No.  1 square is    1 and cube is    1
No.  2 square is    4 and cube is    8
No.  3 square is    9 and cube is   27
No.  4 square is   16 and cube is   64
No.  5 square is   25 and cube is  125
No.  6 square is   36 and cube is  216
No.  7 square is   49 and cube is  343
No.  8 square is   64 and cube is  512
No.  9 square is   81 and cube is  729
No. 10 square is  100 and cube is 1000
No. 11 square is  121 and cube is 1331
No. 12 square is  144 and cube is 1728
No. 13 square is  169 and cube is 2197
No. 14 square is  196 and cube is 2744
No. 15 square is  225 and cube is 3375
No. 16 square is  256 and cube is 4096
No. 17 square is  289 and cube is 4913
No. 18 square is  324 and cube is 5832
No. 19 square is  361 and cube is 6859
>>> for i in range(1,20):
	print("No. {0:2} square is {1:<4} and cube is {2:^4}".format(i,i**2,i**3))

	
No.  1 square is 1    and cube is  1  
No.  2 square is 4    and cube is  8  
No.  3 square is 9    and cube is  27 
No.  4 square is 16   and cube is  64 
No.  5 square is 25   and cube is 125 
No.  6 square is 36   and cube is 216 
No.  7 square is 49   and cube is 343 
No.  8 square is 64   and cube is 512 
No.  9 square is 81   and cube is 729 
No. 10 square is 100  and cube is 1000
No. 11 square is 121  and cube is 1331
No. 12 square is 144  and cube is 1728
No. 13 square is 169  and cube is 2197
No. 14 square is 196  and cube is 2744
No. 15 square is 225  and cube is 3375
No. 16 square is 256  and cube is 4096
No. 17 square is 289  and cube is 4913
No. 18 square is 324  and cube is 5832
No. 19 square is 361  and cube is 6859
>>> for i in range(1,20):
	print("No. {0:2} square is {1:^4} and cube is {2:^4}".format(i,i**2,i**3))

	
No.  1 square is  1   and cube is  1  
No.  2 square is  4   and cube is  8  
No.  3 square is  9   and cube is  27 
No.  4 square is  16  and cube is  64 
No.  5 square is  25  and cube is 125 
No.  6 square is  36  and cube is 216 
No.  7 square is  49  and cube is 343 
No.  8 square is  64  and cube is 512 
No.  9 square is  81  and cube is 729 
No. 10 square is 100  and cube is 1000
No. 11 square is 121  and cube is 1331
No. 12 square is 144  and cube is 1728
No. 13 square is 169  and cube is 2197
No. 14 square is 196  and cube is 2744
No. 15 square is 225  and cube is 3375
No. 16 square is 256  and cube is 4096
No. 17 square is 289  and cube is 4913
No. 18 square is 324  and cube is 5832
No. 19 square is 361  and cube is 6859
>>> for i in range(1,20):
	print("No. {} square is {} and cube is {2}".format(i,i**2,i**3))

	
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    print("No. {} square is {} and cube is {2}".format(i,i**2,i**3))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> 