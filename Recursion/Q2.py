# # . Write a Python program to converting an Integer to a string in any base.

def to_string(n,base):
    conv_str = "0123456789ABCDEF"
    if n < base:
        return conv_str[n]
    else:
        return to_string(n//base,base) + conv_str[n % base]
print(to_string(2835,16))


