# print(round(8/3,2))
# print(8//3)   # Floor Division

# score = 0
# height = 1.8
# isWinning = True
# # F-String
# print(f"your score is {score}, your height is {height}, and your winning is {isWinning}")


age = int(input("Enter your age: "))
year_rem = 90 - age
days_rem = 365 * year_rem
weeks_rem = 52 * year_rem
months_rem = 12 * year_rem
print(f"you have {days_rem} days,{weeks_rem} weeks and {months_rem} months left.")