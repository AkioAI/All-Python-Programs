a=5    #101
b=8    #1000
a=a^b   #11(4bits)1011 #^ advantage of using XOR is that it will not waste extra Bits  #wasting 1 extra bit
b=a^b   #5
a=a^b   #8
print(a)
print(b)
