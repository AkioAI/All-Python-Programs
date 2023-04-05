# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def string_test(s):
    d={"Uppercase":0, "Lowercase":0}
    for i in s:
        if i.isupper():
            d["Uppercase"]+=1
        elif i.islower():
            d["Lowercase"]+=1
        else:
            pass
    print (f"Original String : {s}")
    print ("No. of Upper case characters :", d["Uppercase"])
    print ("No. of Lower case Characters :", d["Lowercase"])
s = 'The quick Brown Fox'
string_test(s)



