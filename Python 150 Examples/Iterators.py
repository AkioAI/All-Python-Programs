list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"," "]
my_iterator=iter(list)
for i in range(1,len(list)):
    next_day=next(my_iterator)
    print(i,"\t",next_day)