countries=["USA","India","Japan","South Korea","Russia"]
print(countries)
str=input("Enter one of the countries: ")
countries_orig=countries.index(str)
print("this country placed on",countries_orig)
num=int(input("Enter number between 0 to 4: "))
print()
print(countries[num])