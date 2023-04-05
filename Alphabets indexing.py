>>> alphabets='abcdefghijklmnopqrstuvwxyz'
>>> backwards=alphabets[::25]
>>> print(backwards)
az
>>> backwards=alphabets[9::25]
>>> print(backwards)
j
>>> backwards=alphabets[-9::-25]
>>> print(backwards)
r
>>> backwards=alphabets[-9::-1]
>>> print(backwards)
rqponmlkjihgfedcba
>>> backwards=alphabets[:9:-1]
>>> print(backwards)
zyxwvutsrqponmlk
>>> backwards=alphabets[-9:-1:-1]
>>> print(backwards)

>>> backwards=alphabets[9:-1:-1]
>>> print(backwards)

>>> backwards=alphabets[9:1:-1]
>>> print(backwards)
jihgfedc
>>> backwards=alphabets[25::-1]
>>> print(backwards)
zyxwvutsrqponmlkjihgfedcba
>>> backwards=alphabets[25:0:-1]
>>> print(backwards)
zyxwvutsrqponmlkjihgfedcb
>>> backwards=alphabets[25:20:-1]
>>> print(backwards)
zyxwv
>>> backwards=alphabets[25:17:-1]
>>> print(backwards)
zyxwvuts
>>> backwards=alphabets[17:14:-1]
>>> print(backwards)
rqp
>>> backwards=alphabets[18:15:-1]
>>> print(backwards)
srq
>>> backwards=alphabets[16:13:-1]
>>> print(backwards)
qpo
>>> backwards=alphabets[4::-1]
>>> backwards=alphabets[4::-1]
>>> print(backwards)
edcba
>>> 