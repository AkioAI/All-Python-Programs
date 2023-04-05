names=input("Enter your name: ")
count=0
for name in names:
    if (name=='a' or name=='A') or (name=='e' or name=='E') or (name=='i' or name=='I') or (name=='o' or name=='O') or (name=='u' or name=='U'):
        count+=1
print("vowels",count)