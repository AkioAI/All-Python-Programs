# 24. Write a Python program to append a list to the second list.

def join_lst(lst1,lst2):
    for elements in lst2:
        lst1.append(elements)
    return lst1
lst1 = ['Python',1, '43',34,213,'Sketching']
lst2 = ['Javascript','Sakura','kisho']
print(join_lst(lst1,lst2))