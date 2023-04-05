pass1=input("Enter a new password: ")
pass2=input("Enter it again: ")
if pass1==pass2:
    print("Thank you!")
elif pass1.upper()==pass2.upper():
    print("They must be in the same case")
else:
    print("Incorrect")