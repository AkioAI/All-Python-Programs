#Guess The Number Game
import random

guessesTaken=0

name=input("What is your name: ")

number=random.randint(1,20)
print("Well.. "+name+" I am Thinking of a number between 1 to 20...")

for guessesTaken in range(6):
    guess=int(input("Take a guess..: "))

    if guess<number:
        print("your guess is too low..")
    if guess>number:
        print("your guess is too high")
    if guess==number:
        break

if guess==number:
    guessesTaken=str(guessesTaken+1)
    print("Good job.." +name+ "! you guess my number in "+guessesTaken+" guesses!")

if guess!=number:
    number=str(number)
    print("Nope! the number i was thinking was " +number+ '.')


