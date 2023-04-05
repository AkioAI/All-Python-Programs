# 20. Write a Python program access the index of a list.

def access_idx(lst):
    for index,i in enumerate(lst,start=1):
        print(f"{index}\t{i}")
lst = ['Manga','Python','Physics','Javascript','Minecraft']
access_idx(lst)
