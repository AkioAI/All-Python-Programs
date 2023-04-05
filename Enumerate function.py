
>>> mynames=["Sam","Pit","Misch"]
>>> for index,myname in enumerate(mynames,start=1)
SyntaxError: invalid syntax
>>> for index,myname in enumerate(mynames,start=1)
SyntaxError: invalid syntax
>>> for index,myname in enumerate(mynames,start=1):
	print(index,myname)

	
1 Sam
2 Pit
3 Misch
>>> 