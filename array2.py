Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from array import*
>>> arr1=array('i',[1,2,3,4,5])
>>> arr2=array('i',[6,7,8,9,10])
>>> arr1.extend(arr2)
>>> print(arr2)
array('i', [6, 7, 8, 9, 10])
>>> print(arr1)
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

>>> 