# Leap Year

# year = int(input("Enter a year: "))
# if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#     print(f"{year} is a Leap Year!")
# else:
#     print(f"{year} is not a leap Year")


# OR

year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a Leap Year!")
        else:
            print(f"{year}Not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
