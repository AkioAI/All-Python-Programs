compnum=50
num = int(input("Guess the number i am thinking?: "))
count=1
while num!=compnum:
    if num<50:
        print("your guess is too low")
    else:
        print("your guess is too high")
    count+=1
