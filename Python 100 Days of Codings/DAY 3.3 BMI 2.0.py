weight = int(input("Enter your weight: "))
height = float(input("Enter your Height in m: "))
BMI = weight/(height**2)
if BMI < 18.5:
    print("You are Underweight.")
elif 18.5<BMI<25:
    print("You have a normal weight.")
elif 25<BMI<30:
    print("You are overweight!")
elif 30<BMI<35:
    print("You are Obese")
else:
    print("you are clinically obese")
print("Your Body Mass Index is: ", int(BMI))