import random

def addition():
    num1=random.randrange(5,20)
    num2=random.randrange(5,20)
    print(num1)
    print(num2)
    user_ans=int(input("Enter your answer: "))
    ans=num1+num2
    print("Your answer is:", user_ans)
    print("My answer is:", ans)
    answers= ( user_ans , ans )
    print(answers)
    return answers
def subtraction():
    num3 = random.randrange(25,50)
    num4 = random.randrange(1,25)
    print(num3)
    print(num4)
    user_ans=int(input("What is your answr: "))
    ans=num3-num4
    print("Your answer is:", user_ans)
    print("My answer is:", ans)
    answers= ( user_ans , ans )
    print(answers)
    return answers
def check_answer(user_ans,ans):
    if user_ans==ans:
        print("Correct!")
    else:
        print("Incorrect! , The answer is", ans)
def display():
    print("1) Addition.\n2) Subtraction.")
    user=int(input("Enter 1 or 2: "))
    if user == 1:
        user_ans, ans = addition()
        check_answer(user_ans,ans)
    elif user == 2:
        user_ans, ans = subtraction()
        check_answer(user_ans, ans)
    else:
        print("Incorrect selection!")
display()
