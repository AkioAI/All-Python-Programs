Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from array import*
>>> import numpy
>>> arr=array('i',[1,2,6,8,9])
>>> print(i)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> print(arr)
array('i', [1, 2, 6, 8, 9])
>>> for i in arr
SyntaxError: invalid syntax
>>> for i in (arr)
SyntaxError: invalid syntax
>>> for i in arr:
	print(i)

	
1
2
6
8
9
>>> 