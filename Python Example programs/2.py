def sumNum(num):
    previousNum=0
    for i in range(num):
        sum=previousNum+i
        print("current number",i,"previous number",previousNum,"and sum is",sum)
        previousNum=i

sumNum(10)

