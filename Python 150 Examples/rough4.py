strings=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
my_string=iter(strings)
for i in range(0,len(strings)):
    print(next(my_string))