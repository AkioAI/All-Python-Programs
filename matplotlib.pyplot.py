Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from numpy import logspace,tan,exp,pi
>>> import matplotlib.pyplot as mp
>>> x=logspace(0,5*pi,500)
>>> y=tan(x)*exp(-x/10)
>>> mp.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002AEDCBB4CD0>]
>>> mp.shor()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mp.shor()
AttributeError: module 'matplotlib.pyplot' has no attribute 'shor'
>>> mp.show()
>>> 